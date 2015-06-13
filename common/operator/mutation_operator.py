#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging
import common.constants as CONST
from common.operator.bit_mutation import BitMutationOperator
from common.operator.int_mutation import IntMutationOperator
from common.operator.permutation_mutation import PermutationMutationOperator

log = logging.getLogger(__name__)


class MutationOperator(object):

    def __init__(self):
        pass

    def configure(self, config):
        '''
        '''
        self.operators = {}

        factor = float(config.mutation_factor)
        bit_mutation = BitMutationOperator(factor)
        perm_mutation = PermutationMutationOperator(factor)
        int_mutation = IntMutationOperator().configure(config)

        self.operators[CONST.BIT_BOX_KEY] = bit_mutation
        self.operators[CONST.PERMUTATION_BOX_KEY] = perm_mutation
        self.operators[CONST.INT_BOX_KEY] = int_mutation

    def mutate(self, solution):
        '''
        '''
        for key in solution.container:
            self.operators[key].mutate(solution.container[key])
