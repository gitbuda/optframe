#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import sys
import numpy
import random
import logging

from common.genotype import Genotype
from helpers.array_tools import swap
from common.lt_population import LTPopulation

log = logging.getLogger(__name__)


def run(config):

    population_size = config.population_size
    solution_size = config.solution_size
    values_number = config.values_number

    log.info("start")
    log.info('Solution size: %s', solution_size)

    population = LTPopulation(solution_size, values_number)

    # generate population
    for solution_index in xrange(population_size):
        genes = [random.randint(0, 1) for i in xrange(solution_size)]
        genes = numpy.array(genes)
        solution = Genotype(genes)
        population.add(solution, recalculate=False)

    max_fitness = -sys.maxsize
    best_genotype = None
    evaluator = config.evaluate_operator
    for solution in population.solutions:
        fitness = evaluator.evaluate(solution.get_genotype())
        solution.set_fitness(fitness)
        if fitness >= max_fitness:
            max_fitness = fitness
            best_genotype = solution
    log.info('Population size: %s', population_size)

    for iteration in xrange(config.iterations):
        log.info('Iteration: %d' % iteration)
        population.recalculate_population()
        linkage_tree = population.get_clusters()
        linkage_tree = sorted(linkage_tree, key=lambda x: len(x), reverse=True)
        log.info('Clusters: %d', len(linkage_tree))
        for cluster in linkage_tree:
            first, second = random.sample(range(population_size), 2)
            a = population.solutions[first]
            b = population.solutions[second]
            off_a, off_b = swap(a.get_genotype(), b.get_genotype(), cluster)
            fit_a = a.get_fitness()
            fit_b = b.get_fitness()
            fit_off_a = evaluator.evaluate(off_a)
            fit_off_b = evaluator.evaluate(off_b)
            if fit_off_a >= fit_a and fit_off_a >= fit_b \
                    and fit_off_b >= fit_a and fit_off_b >= fit_b:
                gen_a = Genotype(off_a, fit_off_a)
                gen_b = Genotype(off_b, fit_off_b)
                population.add(gen_a, recalculate=False)
                population.add(gen_b, recalculate=False)
                if fit_off_a >= max_fitness:
                    max_fitness = fit_off_a
                    best_genotype = gen_a
                if fit_off_b >= max_fitness:
                    max_fitness = fit_off_b
                    best_genotype = gen_b
        log.info('Population size: %s' % str(len(population.solutions)))
        log.info('Best %s' % max_fitness)

    return (best_genotype.get_genotype(), best_genotype.get_fitness())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)