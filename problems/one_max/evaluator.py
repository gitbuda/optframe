# -*- coding: utf-8 -*-

'''
Onemax problem evaluator.
'''

from common.evaluation_counter import EvaluationCounter
from common.fitness import Fitness, MAX
from common.constants import BIT_BOX_KEY


class Evaluator(object):

    def __init__(self):
        '''
        '''
        self.evaluation_counter = EvaluationCounter()

    def configure(self, config=''):
        '''
        '''
        self.evaluation_counter.configure(config)

    def evaluate(self, solution):
        '''
        '''
        self.evaluation_counter.increment()

        solution = solution.container[BIT_BOX_KEY]

        gene_sum = float(sum(solution))

        return Fitness(gene_sum / len(solution), MAX)
