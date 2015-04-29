# -*- coding: utf-8 -*-

'''
Deceptive step trap problem evaluator.
'''

import logging

from common.evaluation_counter import EvaluationCounter

log = logging.getLogger(__name__)


class Config(object):
    '''
    '''
    def __init__(self):
        self.trap_size = 7
        self.step_size = 2
        self.evaluations_number = 100000


class Evaluator(object):

    def __init__(self):
        '''
        '''
        self.evaluation_counter = EvaluationCounter()

    def configure(self, config=''):
        '''
        '''
        self.trap_size = int(config.trap_size)
        self.step_size = int(config.step_size)
        self.offset = (self.trap_size - self.step_size) % self.step_size
        self.trap_max = (self.offset + self.trap_size) / self.step_size
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
            total += (self.offset + partial) / self.step_size

        return total


if __name__ == '__main__':

    evaluator = Evaluator()
    config = Config()
    evaluator.configure(config)
    print evaluator.evaluate([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
