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
    # e.g.
    evaluator = context.evaluate_operator
    solution_size = context.solution_size

    best_store = BestStore()
    best_store.configure(context.config)
    populations = [[]]

    try:
        while True:
            solution = Solution(random_bitstr(solution_size))
            solution.fitness = evaluator.evaluate(solution.box)
            best_store.try_store(solution.fitness, solution)
            populations[0].append(solution)

            for index in xrange(len(populations)):
                population = populations[index]
                population_size = len(population)
                max_edges = 3 * population_size
                network = construct_network(population, solution_size,
                                            max_edges)
                children = sample_from_network(population, network, 1)[0]
                children.fitness = evaluator.evaluate(children.box)
                best_store.try_store(children.fitness, children)
                if children.fitness >= solution.fitness:
                    next_population_index = index + 1
                    if next_population_index == len(populations):
                        populations.append([])
                    next_population = populations[next_population_index]
                    next_population.append(children)
                    solution = children
                else:
                    break
    except Exception as e:
        import traceback
        traceback.print_exc()
        log.info(e)

    return (best_store.best_solution, best_store.best_fitness)


if __name__ == '__main__':
    pass
