#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Run GA algorithm on bool problem.
'''

import sys
import logging
import ga.gaengine as gaengine
from evaluator.bool_array import BoolArrayEvaluator
from ga.gaconfig import GAConfig


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # read GA config file
    config = GAConfig('config/gaconfig_bool.ini')
    config.evaluate_operator = BoolArrayEvaluator()

    (genotype, fitness) = gaengine.run(config)
    print 'Genotype: %s; Fitness: %s' % (genotype, fitness)
