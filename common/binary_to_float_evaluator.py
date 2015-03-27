#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

from helpers.binary_to_float import BinaryToFloatCached


class BinaryToFloatEvaluator(object):

    def __init__(self):
        pass

    def configure(self, config=''):

        self.bits = int(config.bits_per_float)
        self.precision = int(config.precision)
        self.minimum = float(config.minimum)
        self.maximum = float(config.maximum)
        self.solution_size = int(config.solution_size)

        assert self.solution_size % self.bits == 0
        self.n = self.solution_size / self.bits

        self.converter = BinaryToFloatCached(self.bits,
                                             self.minimum,
                                             self.maximum)
        self.function = {}
        self.worst = 0
