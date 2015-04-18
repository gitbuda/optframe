# -*- coding: utf-8 -*-

'''
PGAConfig
'''

import logging

from common.operator.bit_cross import BitCrossOperator
from common.operator.bit_mutation import BitMutationOperator
from common.operator.bit_box import BitBoxOperator
from common.operator.permutation_cross import PermutationCrossOperator
from common.operator.permutation_mutation import PermutationMutationOperator
from common.operator.permutation_box import PermutationBoxOperator

log = logging.getLogger(__name__)


class Config(object):

    def __init__(self):
        self.parameters = {}

    def load_problem_conf(self, problem_config):
        self.config = problem_config

        if 'solution_type' in self.config:
            self.config.weak_set('cross_operator',
                                 '%sCrossOperator' %
                                 self.config.solution_type)
            self.config.weak_set('mutation_operator',
                                 '%sMutationOperator' %
                                 self.config.solution_type)
            self.config.weak_set('box_operator',
                                 '%sBoxOperator' %
                                 self.config.solution_type)

    def load_algorithm_conf(self, algorithm_config):

        self.config.weak_merge(algorithm_config)

        self.mutation_factor = float(self.config.mutation_factor)
        self.cross_factor = float(self.config.crossover_factor)
        self.solution_number = int(self.config.solution_number)
        self.solution_size = int(self.config.solution_size)

        # load all operators
        self.box_operators = {}
        self.box_operators['bitBoxOperator'] = \
            BitBoxOperator(self.solution_size)
        self.box_operators['permutationBoxOperator'] = \
            PermutationBoxOperator(self.solution_size)

        self.cross_operators = {}
        self.cross_operators['bitCrossOperator'] = \
            BitCrossOperator(self.cross_factor)
        self.cross_operators['permutationCrossOperator'] = \
            PermutationCrossOperator()

        self.mutation_operators = {}
        self.mutation_operators['bitMutationOperator'] = \
            BitMutationOperator(self.mutation_factor)
        self.mutation_operators['permutationMutationOperator'] = \
            PermutationMutationOperator(self.mutation_factor)

        # choose all operators
        self.box_operator = \
            self.box_operators[self.config.box_operator]
        self.mutation_operator = \
            self.mutation_operators[self.config.mutation_operator]
        self.cross_operator = \
            self.cross_operators[self.config.cross_operator]

        log.info('PGA configuration loaded.')
