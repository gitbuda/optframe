#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Run P3 algorithm.
'''

import sys
import logging
from p3 import p3engine
from p3config import P3Config
from evaluator.tsp import TSPEvaluator


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    try:
        iterations = int(sys.argv[1])
    except:
        iterations = 1

    for i in xrange(iterations):
        config = P3Config('config/p3config_tsp.ini')
        config.evaluator = TSPEvaluator('data/bays29.tsp')
        p3engine.run(config)
