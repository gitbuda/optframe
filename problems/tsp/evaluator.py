# -*- coding: utf-8 -*-

'''
TSP problem evaluator.
'''

import sys
import common.constants as CONST
from common.fitness import Fitness, MIN
from problems.tsp.tsplib_loader import TSPLibLoader
from common.evaluation_counter import EvaluationCounter


class Evaluator(object):

    def __init__(self):
        '''
        '''
        self.evaluation_counter = EvaluationCounter()
        self.loader = TSPLibLoader()

    def configure(self, config=''):
        '''
        '''
        self.evaluation_counter.configure(config)
        path = config.input_file_path
        self.tsp = self.loader.load(path)

    def evaluate(self, solution):
        '''
        '''
        self.evaluation_counter.increment()

        cost = 0
        genotype = solution.container[CONST.PERMUTATION_BOX_KEY]
        length = len(genotype)
        unique = set()

        for i, item in enumerate(genotype):

            if item in unique:
                return self.theworst_fitness()

            if i + 1 == length:
                next_item = 0
            else:
                next_item = genotype[i + 1]

            unique.add(item)

            cost += self.tsp.distances[item][next_item]

        return Fitness(cost, MIN)

    def theworst_fitness(self):
        '''
        '''
        return Fitness(sys.maxsize, MIN)
