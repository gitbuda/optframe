#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

import common.constants as CONST
from .array.operator import Operator as ArrayCross
from .permutation.operator import Operator as PermCross

log = logging.getLogger(__name__)


class Operator(object):

    def __init__(self):
        '''
        '''
        pass

    def configure(self, context):
        '''
        '''
        self.evaluator = context.evaluate_operator

        self.operators = {}

        array_cross = ArrayCross()
        array_cross.configure(self.evaluator)
        self.operators[CONST.BIT_BOX_KEY] = array_cross

        perm_cross = PermCross()
        perm_cross.configure(self.evaluator)
        self.operators[CONST.PERMUTATION_BOX_KEY] = perm_cross

        self.operators[CONST.INT_BOX_KEY] = array_cross

    def cross(self, solution, donors, clusters):
        '''
        '''
        for box in solution.container:
            self.operators[box].cross(box, solution, donors, clusters[box])


if __name__ == '__main__':
    pass
