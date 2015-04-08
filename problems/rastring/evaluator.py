# -*- coding: utf-8 -*-

'''
Rastring function evaluator
http://www.cs.unm.edu/~neal.holts/dga/benchmarkFunction/rastrigin.html
'''

import math

from itertools import islice
from helpers.calculator import float_round
from common.evaluation_counter import EvaluationCounter
from common.binary_to_float_evaluator import BinaryToFloatEvaluator


class Evaluator(BinaryToFloatEvaluator):

    def __init__(self):
        '''
        '''
        self.evaluation_counter = EvaluationCounter()

    def configure(self, config=''):
        '''
        '''
        super(Evaluator, self).configure(config)
        self.evaluation_counter.configure(config)

        for x in self.converter.values:
            fvalue = 10 + x**2 - (10 * math.cos(2 * math.pi * x))
            self.function[x] = fvalue
            if self.worst < fvalue:
                self.worst = fvalue

    def evaluate(self, solution):
        '''
        '''
        self.evaluation_counter.increment()

        total = 0
        it = iter(solution)
        while True:
            next_n = list(islice(it, self.bits))
            x = self.converter.convert(next_n)
            if not next_n:
                break
            total += self.function[x]

        total /= (self.n * self.worst)
        return - float_round(1 - total, self.precision)
