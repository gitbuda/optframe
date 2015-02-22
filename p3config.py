# -*- coding: utf-8 -*-

'''
P3Config
'''

import logging
from config import read

from p3.evaluator.bool_array import BoolArrayEvaluator
from p3.evaluator.tsp import TSPEvaluator
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


class P3Config(object):

    def __init__(self):

        self._settings = read('data/p3config.ini')

        log = logging.getLogger(__name__)

        self.genotype_size = int(self._settings.get(SECTION, GENOTYPE_SIZE))
        log.info('Genotype size: %s' % self.genotype_size)
        self.solution_no = int(self._settings.get(SECTION, SOLUTION_NO))
        log.info('Solution number: %s' % self.solution_no)
        self.values_no = int(self._settings.get(SECTION, VALUES_NO))
        log.info('Values number: %s' % self.values_no)
        self.genotype_type = self._settings.get(SECTION, GENOTYPE_TYPE)
        log.info('Genotype type: %s' % self.genotype_type)
        self.evaluator_name = self._settings.get(SECTION, EVALUATOR)
        log.info('Evaluator name: %s' % self.evaluator_name)
        self.booster_name = self._settings.get(SECTION, BOOSTER)
        log.info('Booster name: %s' % self.booster_name)
        self.mixer_name = self._settings.get(SECTION, MIXER)
        log.info('Mixer name: %s' % self.mixer_name)

        self.operators = {}
        self.operators['BoolArrayEvaluator'] = \
            BoolArrayEvaluator()
        self.operators['TSPEvaluator'] = \
            TSPEvaluator('data/bays29.tsp')
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
        self.evaluator = self.operators[self.evaluator_name]
        self.booster = self.operators[self.booster_name]
        self.mixer = self.operators[self.mixer_name]
