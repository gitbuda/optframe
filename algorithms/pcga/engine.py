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
    best_store = context.best_store

    try:
        # algorithm
        cpv = CompactProbabilityVector(solution_size)
        zero_population = PCGAPopulation(cpv)
        # 4 because then update value is 1 / 4, it seems
        # for me like a good value, TODO: check is this
        # ok value and if neccessary create a better one
        zero_population.size = 4
        populations = [zero_population]

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
                cpv.update_vector(winner, loser, population.size)
                if winner.fitness > solution.fitness:
                    next_population_index = index + 1
                    if next_population_index == len(populations):
                        new_cpv = CompactProbabilityVector(solution_size)
                        new_population = PCGAPopulation(new_cpv)
                        # the population size grows expenentialy
                        # also it seems to me like good TODO: check this
                        new_population.size = population.size * 2
                        populations.append(new_population)
                    solution = winner

    except Exception as e:
        import traceback
        traceback.print_exc()
        log.info(e)

    solution = best_store.best_solution

    log.info("PCGA: %s" % solution.fitness.value)

    return solution


if __name__ == '__main__':
    pass
