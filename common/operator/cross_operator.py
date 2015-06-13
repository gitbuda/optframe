#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging
import common.constants as CONST

from common.operator.bit_cross import BitCrossOperator
from common.operator.permutation_cross import PermutationCrossOperator
from common.solution import Solution

log = logging.getLogger(__name__)


class CrossOperator(object):

    def __init__(self):
        pass

    def configure(self, config):
        '''
        '''
        self.operators = {}
        bit_cross = BitCrossOperator(float(config.cross_factor))
        self.operators[CONST.BIT_BOX_KEY] = bit_cross
        self.operators[CONST.PERMUTATION_BOX_KEY] = PermutationCrossOperator()
        # TODO: replace with IntCrossOperator
        self.operators[CONST.INT_BOX_KEY] = bit_cross

    def cross(self, better, worse):
        '''
        '''
        solution = Solution({})
        for key in better.container:
            better_box = better.container[key]
            worse_box = worse.container[key]
            solution.container[key] = \
                self.operators[key].cross(better_box, worse_box)
        return solution
