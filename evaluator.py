# -*- coding: utf-8 -*-

'''
Deceptive trap problem evaluator.
'''

import logging

from common.evaluation_counter import EvaluationCounter


class Config(object):
    '''
    Only for local test.
    '''
    def __init__(self):
        self.trap_size = 3


class Evaluator(object):

    def __init__(self):
        '''
        '''
        self.evaluation_counter = EvaluationCounter()

    def configure(self, config=''):
        '''
        '''
        self.trap_size = int(config.trap_size)
        self.evaluation_counter.configure(config)

    def evaluate(self, solution):
        '''
        '''
        self.evaluation_counter.increment()

        total = 0

        for i in xrange(0, len(solution), self.trap_size):
            partial = 0
            trap_end_i = i + self.trap_size
            if trap_end_i > len(solution):
                trap_end_i = len(solution)
            for index in xrange(i, trap_end_i):
                partial += solution[index]
            if partial < self.trap_size:
                partial = self.trap_size - partial - 1
            total += partial

        return total


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    evaluator = Evaluator()
    config = Config()
    evaluator.configure(config)
    print evaluator.evaluate([1, 1, 1, 1, 1, 1, 1, 1, 1])
