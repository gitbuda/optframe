#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
PCGA - Pyramid Compact Genetic Algorithm

Variation of CGA in which exists pyramid population structure.
'''

import random
import logging

from common.best_store import BestStore
from common.solution import Solution
from common.cpv import CompactProbabilityVector

log = logging.getLogger(__name__)


class PCGAPopulation(object):

    def __init__(self, cpv):
        self.cpv = cpv
        self.size = 0

    def increment_size(self):
        self.size += 1


def run(context):
    '''
    '''
    solution_size = context.solution_size
    evaluator = context.evaluate_operator

    best_store = BestStore()
    best_store.configure(context.config)

    try:
        # algorithm
        cpv = CompactProbabilityVector(solution_size)
        populations = [PCGAPopulation(cpv)]

        while True:
            solution = Solution([random.randint(0, 1)
                                for x in xrange(solution_size)])
            solution.fitness = evaluator.evaluate(solution.box)
            best_store.try_store(solution.fitness, solution)

            for index in xrange(len(populations)):
                population = populations[index]
                cpv = population.cpv
                candidate = cpv.generate_candidate()
                candidate.fitness = evaluator.evaluate(candidate.box)
                if solution.fitness > candidate.fitness:
                    winner, loser = (solution, candidate)
                else:
                    winner, loser = (candidate, solution)
                best_store.try_store(winner.fitness, winner)
                population.increment_size()
                cpv.update_vector(winner, loser, population.size)
                if winner.fitness > solution.fitness:
                    next_population_index = index + 1
                    if next_population_index == len(populations):
                        new_cpv = CompactProbabilityVector(solution_size)
                        populations.append(PCGAPopulation(new_cpv))
                    solution = winner
                else:
                    break

    except Exception as e:
        log.info(best_store.best_solution.box)
        log.info(e)

    return (best_store.best_solution, best_store.best_fitness)


if __name__ == '__main__':
    pass
