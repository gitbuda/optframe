#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Framework specific bit cross operator.
'''

import random

from common.operator.cross.ux import UXCrossOperator
from common.operator.cross.twopoint import TwoPointCrossOperator


class BitCrossOperator(object):

    def __init__(self, cross_factor):
        '''
        Setup all bit cross operators.
        '''
        self.operators = []
        self.operators.append(UXCrossOperator(cross_factor))
        self.operators.append(TwoPointCrossOperator())
        self.operators_range = len(self.operators) - 1

    def cross(self, genotype_better, genotype_worse):
        '''
        Make crossover and return result.
        '''
        operator_index = random.randint(0, self.operators_range)
        operator = self.operators[operator_index]

        new_genotype = operator.cross(genotype_better, genotype_worse)

        return new_genotype
