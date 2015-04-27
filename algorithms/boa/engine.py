#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

from common.best_store import BestStore
from common.solution import Solution
from common.bayes.network import random_bitstr
from common.bayes.network import construct_network
from common.bayes.network import sample_from_network

log = logging.getLogger(__name__)


def run(context):
    '''
    '''
    evaluator = context.evaluate_operator
    solution_size = context.solution_size
    iterations_number = context.iterations_number
    population_size = context.population_size
    select_size = context.select_size
    childern_number = context.childern_number
    max_edges = 3 * population_size

    best_store = BestStore()
    best_store.configure(context.config)

    try:

        population = [Solution(x, evaluator.evaluate(x)) for x in
                      [random_bitstr(solution_size) for y in
                      xrange(population_size)]]
        best = sorted(population, key=lambda x: x.fitness, reverse=True)[0]
        for iteration in xrange(iterations_number):
            selected = population[:select_size]
            network = construct_network(selected, solution_size, max_edges)
            childrens = sample_from_network(selected, network, childern_number)
            for children in childrens:
                children.fitness = evaluator.evaluate(children.box)
            population = population[0:(population_size - select_size)] \
                + childrens
            population_size = len(population)
            max_edges = 3 * population_size
            population.sort(key=lambda x: x.fitness, reverse=True)
            first = population[0]
            print 'Best solution: %s Fitness %s' % (first.box,
                                                    first.fitness)
            if first.fitness > best.fitness:
                best = first

    except Exception:
        pass

    return best.box, best.fitness


if __name__ == '__main__':
    pass
