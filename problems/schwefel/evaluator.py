# -*- coding: utf-8 -*-

'''
Schwefel function evaluator
http://www.cs.unm.edu/~neal.holts/dga/benchmarkFunction/schwefel.html
'''

import math
from itertools import islice
from helpers.calculator import float_round
from common.binary_to_float_evaluator import BinaryToFloatEvaluator


class Evaluator(BinaryToFloatEvaluator):

    def __init__(self):
        self.evaluations_number = 0

    def configure(self, config=''):
        super(Evaluator, self).configure(config)

        self.alpha = float(config.alpha)

        for x in self.converter.values:
            fvalue = x * math.sin(math.sqrt(math.fabs(x))) + self.alpha
            self.function[x] = fvalue
            if self.worst < fvalue:
                self.worst = fvalue

    def evaluate(self, solution):
        self.evaluations_number += 1

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
