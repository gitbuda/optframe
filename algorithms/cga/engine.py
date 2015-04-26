#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Compact Genetic Algorithm
'''

import logging

from common.best_store import BestStore
from common.cpv import CompactProbabilityVector

log = logging.getLogger(__name__)


def run(context):
    '''
    '''
    solution_size = context.solution_size
    population_size = context.population_size
    iterations_number = context.iterations_number
    evaluator = context.evaluate_operator

    best_store = BestStore()
    best_store.configure(context.config)

    try:
        cpv = CompactProbabilityVector(solution_size)
        for iteration in xrange(iterations_number):
            c1 = cpv.generate_candidate()
            c1.fitness = evaluator.evaluate(c1.box)
            c2 = cpv.generate_candidate()
            c2.fitness = evaluator.evaluate(c2.box)
            winner, loser = (c1, c2) if c1.fitness > c2.fitness else (c2, c1)
            best_store.try_store(winner.fitness, winner)
            cpv.update_vector(winner, loser, population_size)
    except Exception:
        pass

    return (best_store.best_solution, best_store.best_fitness)


if __name__ == '__main__':
    pass
