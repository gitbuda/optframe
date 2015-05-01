#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import random
import logging

from common.constants import BIT_BOX_KEY

log = logging.getLogger(__name__)


class LocalSearch(object):

    def __init__(self):
        '''
        '''
        pass

    def configure(self, context):
        '''
        '''
        self.evaluator = context.evaluate_operator
        self.size = context.solution_size

    def search(self, solution):
        '''
        '''
        # initialize state from solution
        bitstr = list(solution.box[BIT_BOX_KEY])
        fitness = solution.fitness

        # do local search
        new_bitstr = [random.randint(0, 1) for x in xrange(self.size)]
        solution.box[BIT_BOX_KEY] = new_bitstr
        new_fitness = self.evaluator.evaluate(solution)

        # TODO: min max fitness
        if fitness < new_fitness:
            solution.fitness = new_fitness
        else:
            solution.box[BIT_BOX_KEY] = bitstr

        return solution


if __name__ == '__main__':
    pass
