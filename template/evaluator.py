# -*- coding: utf-8 -*-

'''
Evaluator template.

optframe/problems/PROBLEM_NAME/evaluator.py
'''

from common.evaluation_counter import EvaluationCounter


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

        return 0
