# -*- coding: utf-8 -*-

'''
Schwefel function evaluator
http://www.cs.unm.edu/~neal.holts/dga/benchmarkFunction/schwefel.html
'''

import math
from itertools import islice
from helpers.calculator import float_round
from common.evaluation_counter import EvaluationCounter
from common.binary_to_float_evaluator import BinaryToFloatEvaluator
from common.fitness import Fitness, MIN
from common.constants import BIT_BOX_KEY


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

        self.alpha = float(config.alpha)

        for x in self.converter.values:
            fvalue = x * math.sin(math.sqrt(math.fabs(x))) + self.alpha
            self.function[x] = fvalue
            if self.worst < fvalue:
                self.worst = fvalue

    def evaluate(self, solution):
        '''
        '''
        self.evaluation_counter.increment()
        solution = solution.container[BIT_BOX_KEY]

        total = 0

        it = iter(solution)
        while True:
            next_n = list(islice(it, self.bits))
            x = self.converter.convert(next_n)
            if not next_n:
                break
            total += self.function[x]
        total /= (self.n * self.worst)

        return Fitness(float_round(1 - total, self.precision), MIN)
