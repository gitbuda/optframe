#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging
import common.constants as CONST

from common.operator.bit_mutation import BitMutationOperator
from common.operator.permutation_mutation import PermutationMutationOperator

log = logging.getLogger(__name__)


class MutationOperator(object):

    def __init__(self):
        pass

    def configure(self, config):
        '''
        '''
        self.operators = {}
        self.operators[CONST.BIT_BOX_KEY] = \
            BitMutationOperator(float(config.mutation_factor))
        self.operators[CONST.PERMUTATION_BOX_KEY] = \
            PermutationMutationOperator(float(config.mutation_factor))

    def mutate(self, solution):
        '''
        '''
        for key in solution.container:
            self.operators[key].mutate(solution.container[key])
