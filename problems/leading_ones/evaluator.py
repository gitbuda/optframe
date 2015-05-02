# -*- coding: utf-8 -*-

'''
Leading ones problem evaluator.
e.g.
[1, 1, 0, 1, 1] -> 2 -> (normalized) -> 0.4
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
        Calculates normalized sum of leading ones
        in a bit string solution.
        If this function receive solution that is not
        a bit string it will return wrong value (1.0).
        Bitstring check operation is expensive and here
        isn't a place where this should be chacked.
        '''

        self.evaluation_counter.increment()

        bits = solution.container[BIT_BOX_KEY]
        # print bits

        ones = 0
        for bit in bits:
            if bit != 1:
                break
            ones += bit

        return Fitness(1.0 * ones / len(bits), MAX)
