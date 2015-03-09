# -*- coding: utf-8 -*-

'''
P3Config
'''

import logging
from helpers.config import read

from p3.genotype.bit_array import BitArrayGenotype
from p3.genotype.permutation import PermutationGenotype
from p3.booster.bit_array import BitArrayBooster
from p3.booster.permutation import PermutationBooster
from p3.mix.bit_array import BitArrayMix
from p3.mix.permutation import PermutationMix

SECTION = 'P3'
GENOTYPE_SIZE = 'GenotypeSize'
SOLUTION_NO = 'SolutionNo'
VALUES_NO = 'ValuesNo'
GENOTYPE_TYPE = 'GenotypeType'
EVALUATOR = 'Evaluator'
BOOSTER = 'Booster'
MIXER = 'Mixer'
OUTPUT_DIR = 'OutputDir'


class P3Config(object):

    def __init__(self, path='data/p3config.ini'):

        self._settings = read(path)

        log = logging.getLogger(__name__)

        self.genotype_size = int(self._settings.get(SECTION, GENOTYPE_SIZE))
        log.info('Genotype size: %s' % self.genotype_size)
        self.solution_no = int(self._settings.get(SECTION, SOLUTION_NO))
        log.info('Solution number: %s' % self.solution_no)
        self.values_no = int(self._settings.get(SECTION, VALUES_NO))
        log.info('Values number: %s' % self.values_no)
        self.genotype_type = self._settings.get(SECTION, GENOTYPE_TYPE)
        log.info('Genotype type: %s' % self.genotype_type)
        self.booster_name = self._settings.get(SECTION, BOOSTER)
        log.info('Booster name: %s' % self.booster_name)
        self.mixer_name = self._settings.get(SECTION, MIXER)
        log.info('Mixer name: %s' % self.mixer_name)
        self.output_dir = self._settings.get(SECTION, OUTPUT_DIR)

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

        log.info('Configuration loaded.\n')
