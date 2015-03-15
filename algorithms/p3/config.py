# -*- coding: utf-8 -*-

'''
P3Config
'''

import logging

from algorithms.p3.genotype.bit_array import BitArrayGenotype
from algorithms.p3.genotype.permutation import PermutationGenotype
from algorithms.p3.booster.bit_array import BitArrayBooster
from algorithms.p3.booster.permutation import PermutationBooster
from algorithms.p3.mix.bit_array import BitArrayMix
from algorithms.p3.mix.permutation import PermutationMix


class Config(object):

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.parameters = {}

    def load_problem_conf(self, problem_config):
        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):
        self.config.weak_merge(algorithm_config)
        print self.config

        self.genotype_size = int(self.config.solution_size)
        self.log.info('Genotype size: %s' % self.genotype_size)

        self.solution_no = int(self.config.solution_number)
        self.log.info('Solution number: %s' % self.solution_no)

        self.values_no = int(self.config.values_number)
        self.log.info('Values number: %s' % self.values_no)

        solution_type = self.config.solution_type

        self.genotype_type = '%sGenotype' % solution_type
        self.log.info('Genotype type: %s' % self.genotype_type)

        self.booster_name = '%sBooster' % solution_type
        self.log.info('Booster name: %s' % self.booster_name)

        self.mixer_name = '%sMix' % solution_type
        self.log.info('Mixer name: %s' % self.mixer_name)

        self.output_dir = self.config.output_path

        self.operators = {}
        self.operators['BitArrayGenotype'] = \
            BitArrayGenotype
        self.operators['PermutationGenotype'] = \
            PermutationGenotype
        self.operators['BitArrayBooster'] = \
            BitArrayBooster()
        self.operators['PermutationBooster'] = \
            PermutationBooster(4)
        self.operators['BitArrayMix'] = \
            BitArrayMix()
        self.operators['PermutationMix'] = \
            PermutationMix()

        self.genotype = self.operators[self.genotype_type]
        self.booster = self.operators[self.booster_name]
        self.mixer = self.operators[self.mixer_name]

        self.log.info('Configuration loaded.\n')
