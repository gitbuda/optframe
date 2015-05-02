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

    def search(self, solution):
        '''
        '''
        # initialize state from solution
        bitstr = solution.container[BIT_BOX_KEY]
        fitness = solution.fitness
        size = len(solution.container[BIT_BOX_KEY])

        # do local search
        options = [x for x in range(size)]
        tried = set()
        improvement = True
        while improvement:
            improvement = False
            random.shuffle(options)
            for index in options:
                if index in tried:
                    continue
                bitstr[index] = 0 if bitstr[index] == 1 else 1
                new_fitness = self.evaluator.evaluate(solution)
                if fitness < new_fitness:
                    fitness = new_fitness
                    improvement = True
                    tried = set()
                else:
                    bitstr[index] = 0 if bitstr[index] == 1 else 1
                tried.add(index)
        solution.fitness = fitness

        return solution


if __name__ == '__main__':
    pass
