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
        self.operators[CONST.BIT_BOX_KEY] = \
            BitCrossOperator(float(config.cross_factor))
        self.operators[CONST.PERMUTATION_BOX_KEY] = PermutationCrossOperator()

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
