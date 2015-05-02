#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
PCGA - Pyramid Compact Genetic Algorithm

Variation of CGA in which exists pyramid population structure.
Algorithm works only with a bit string solution representation.
Algorithm has no parameters.
'''

import random
import logging

from common.best_store import BestStore
from common.solution import Solution
from common.cpv import CompactProbabilityVector
from common.constants import BIT_BOX_KEY

log = logging.getLogger(__name__)


class PCGAPopulation(object):

    def __init__(self, cpv):
        '''
        Contains PCGA population informations.

        Args:
            cpv: compact probability vector
            size: number of cpv's updates
        '''
        self.cpv = cpv
        self.size = 0

    def increment_size(self):
        '''
        Increment number of cpv's updates.
        '''
        self.size += 1


def run(context):
    '''
    The algorithm:
        1) generate initial solution (solution)
        2) generate solution from pyramid level (candidate)
        3) compare them -> winner, loser
        4) update Compact Probability Vector (cpv) from current pyramid level
        5) if winner is better than solution go to the next pyramid level
    '''
    # initialize algorithm from context
    solution_size = context.solution_size
    evaluator = context.evaluate_operator

    # initialize solution store from the context
    best_store = BestStore()
    best_store.configure(context.config)

    try:
        # algorithm
        cpv = CompactProbabilityVector(solution_size)
        populations = [PCGAPopulation(cpv)]

        while True:
            # TODO: add greedy operator
            solution = Solution({BIT_BOX_KEY: [random.randint(0, 1)
                                for x in xrange(solution_size)]})
            solution.fitness = evaluator.evaluate(solution)
            best_store.try_store(solution)

            for index in xrange(len(populations)):
                population = populations[index]
                cpv = population.cpv
                candidate = cpv.generate_candidate()
                candidate.fitness = evaluator.evaluate(candidate)
                if solution.fitness > candidate.fitness:
                    winner, loser = (solution, candidate)
                else:
                    winner, loser = (candidate, solution)
                best_store.try_store(winner)
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
        log.info(e)

    return best_store.best_solution


if __name__ == '__main__':
    pass
