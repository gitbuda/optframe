#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Framework specific permutation cross operator.
'''

import random

from algorithms.ga.cross.ox_permutation import OXCrossOperator
from algorithms.ga.cross.pmx_permutation import PMXCrossOperator


class PermutationCrossOperator(object):

    def __init__(self):
        '''
        '''
        self.operators = []
        self.operators.append(OXCrossOperator())
        self.operators.append(PMXCrossOperator())
        self.operators_range = len(self.operators) - 1

    def cross(self, genotype_better, genotype_worse):
        '''
        Choose random operator and generate new_genotype.
        '''
        operator_index = random.randint(0, self.operators_range)
        operator = self.operators[operator_index]

        new_genotype = operator.cross(genotype_better, genotype_worse)

        return new_genotype
