# -*- coding: utf-8 -*-

'''
Deceptive trap problem evaluator.
'''

import logging
import common.constants as CONST
from common.fitness import Fitness, MAX
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
        bit_array = solution.container[CONST.BIT_BOX_KEY]
        size = len(bit_array)

        total = 0

        for i in xrange(0, size, self.trap_size):
            partial = 0
            trap_end_i = i + self.trap_size
            if trap_end_i > size:
                trap_end_i = size
            for index in xrange(i, trap_end_i):
                partial += bit_array[index]
            if partial < self.trap_size:
                partial = self.trap_size - partial - 1
            total += partial

        return Fitness(1.0 * total / size, MAX)


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    evaluator = Evaluator()
    config = Config()
    evaluator.configure(config)
    print evaluator.evaluate([1, 1, 1, 1, 1, 1, 1, 1, 1])
