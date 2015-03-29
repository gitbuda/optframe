#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import uuid
import numpy as np

from helpers.solution_writer import SolutionWriter
from algorithms.p3.utils.hashable import hashable
from common.lt_population import LTPopulation

log = logging.getLogger(__name__)


def best_so_far(populations, evaluator):
    # something works :)
    max_fitness = -sys.maxsize
    sum_pop = 0
    best_genotype = []
    for population in populations:
        sum_pop += len(population.solutions)
    # log.info("solutions sum: %d" % sum_pop)
    for i, population in enumerate(populations):
        # log.info('Population %s: %s' % (i, len(population.solutions)))
        for solution in population.solutions:
            genotype = solution.get_genotype()
            fitness = evaluator.evaluate(genotype)
            if max_fitness < fitness:
                max_fitness = fitness
                best_genotype = genotype
    return (max_fitness, best_genotype)


def run(config):

    evaluator = config.evaluate_operator
    mixer = config.mixer
    # booster = config.booster
    genotype = config.genotype
    solution_operator = config.solution_operator
    writer = SolutionWriter()

    solutions = set()
    populations = [LTPopulation(config.genotype_size, config.values_no)]

    while True:

        solution = genotype(config.genotype_size)

        # TODO: remove from here, define specific operator
        if config.problem.problem == 'pipeline':
            gen_gen = solution_operator.next()
            solution.set_genotype(np.array(gen_gen))
        # ------------------------------------------------

        fitness = evaluator.evaluate(solution.get_genotype())
        solution.set_fitness(fitness)

        # solution = booster.boost(solution, evaluator)

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
                        populations.append(LTPopulation(config.genotype_size,
                                                        config.values_no))
                    populations[next_population_index].add(solution)
                    log.info("Added to %d with fitness %f" %
                             (next_population_index, new_fitness))
            else:
                break

        # (max_fitness, best_genotype) = best_so_far(populations, evaluator)
        # print max_fitness, best_genotype

        log.info("End of pyramid iteration\n")
        if len(solutions) >= config.solution_no:
            break

    (max_fitness, best_genotype) = best_so_far(populations, evaluator)

    log.info("Best fitness: " + str(max_fitness))
    output_path = '%s/f%s-%s.solution' % (config.output_dir,
                                          max_fitness, uuid.uuid4().hex)
    log.info("Output path: " + output_path)
    writer.write(output_path, best_genotype, max_fitness)

    return (best_genotype, max_fitness)
