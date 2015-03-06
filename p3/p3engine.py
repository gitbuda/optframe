#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import logging
import uuid

from writer.solution import SolutionWriter
from utils.hashable import hashable
from collections import defaultdict
from clustering import upgma


class P3Population:

    def __init__(self, size, values_no):

        self.size = size
        self.values_no = values_no
        self.solutions = []

        self.occurrences = defaultdict(lambda: defaultdict(list))
        self.pairwise_distance = [[0] * self.size] * self.size

        self.clusters = [[]] * (2 * self.size - 1)

    def get_clusters(self):
        return self.clusters

    def add(self, solution):

        self.solutions.append(solution)
        genotype = solution.get_genotype()

        for i in range(len(solution.get_genotype()) - 1):
            for j in range(i + 1, len(solution.get_genotype())):
                if not self.occurrences[i][j]:
                    self.occurrences[i][j] = [0] * \
                        self.values_no * self.values_no
                entry = self.occurrences[i][j]
                index = genotype[j] * self.values_no + genotype[i]
                entry[index] += 1
                self.update_entropy(i, j, entry)

        self.rebuild_tree()

    def update_entropy(self, i, j, entry):
        total_size = self.values_no * 2
        bits = [0] * total_size
        for k in range(self.values_no):
            for l in range(self.values_no):
                bits[k] += entry[k + l * self.values_no]
        for k in range(self.values_no):
            for l in range(self.values_no):
                bits[self.values_no + k] += entry[k * self.values_no + l]
        total = sum(entry)
        separate = neg_entropy(bits, total)
        together = neg_entropy(entry, total)
        ratio = float(0)
        if together:
            ratio = 2 - (separate / together)
        self.pairwise_distance[i][j] = ratio

    def get_distance(self, i, j):

        if (i > j):
            tmp = i
            i = j
            j = tmp
        return self.pairwise_distance[i][j]

    def rebuild_tree(self):

        (clusters, _) = upgma.build_clusters(self.pairwise_distance)

        self.clusters = clusters


def neg_entropy(counts, total):
    sum_all = 0
    for value in counts:
        if value:
            p = float(value) / total
            sum_all += p * math.log(p, 2)
    return sum_all


def run(config):

    log = logging.getLogger(__name__)

    evaluator = config.evaluator
    mixer = config.mixer
    booster = config.booster
    genotype = config.genotype
    writer = SolutionWriter()

    solutions = set()
    populations = [P3Population(config.genotype_size, config.values_no)]

    while True:

        solution = genotype(config.genotype_size)
        fitness = evaluator.evaluate(solution.get_genotype())
        solution.set_fitness(fitness)

        # skip this step for now
        solution = booster.boost(solution, evaluator)

        if hashable(solution.get_genotype()) not in solutions:
            solutions.add(hashable(solution.get_genotype()))
            populations[0].add(solution)

        for population_index in xrange(len(populations)):
            log.info("Population index: %s population len: %s" %
                     (population_index, len(populations)))
            population = populations[population_index]
            old_fitness = float(solution.get_fitness())
            log.info("Fitness before p3 core: %s" % old_fitness)
            mixer.mix(solution, population, evaluator)
            new_fitness = solution.get_fitness()
            if new_fitness >= old_fitness:
                if hashable(solution.get_genotype()) not in solutions:
                    solutions.add(hashable(solution.get_genotype()))
                    next_population_index = population_index + 1
                    if next_population_index == len(populations):
                        populations.append(P3Population(config.genotype_size,
                                                        config.values_no))
                    populations[next_population_index].add(solution)
                    log.info("Added to %d with fitness %d" %
                             (next_population_index, new_fitness))

        log.info("End of pyramid iteration\n")

        if len(solutions) >= config.solution_no:
            break

    # something works :)
    max_fitness = -sys.maxsize
    sum_pop = 0
    best_genotype = []
    for population in populations:
        sum_pop += len(population.solutions)
    log.info("solutions sum: %d" % sum_pop)
    for i, population in enumerate(populations):
        log.info('Population %s: %s' % (i, len(population.solutions)))
        for solution in population.solutions:
            genotype = solution.get_genotype()
            fitness = evaluator.evaluate(genotype)
            if max_fitness < fitness:
                max_fitness = fitness
                best_genotype = genotype
    log.info("Best fitness: " + str(max_fitness))
    output_path = '%s/%s-%s.solution' % (config.output_dir,
                                         max_fitness, uuid.uuid4().hex)
    log.info("Output path: " + output_path)
    writer.write(output_path, best_genotype, max_fitness)
