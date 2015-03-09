#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Run P3 algorithm.
'''

import sys
import logging
from p3 import p3engine
from p3.p3config import P3Config
from evaluator.bool_array import BoolArrayEvaluator


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    try:
        iterations = int(sys.argv[1])
    except:
        iterations = 1

    for i in xrange(iterations):
        config = P3Config('config/p3config_bool.ini')
        config.evaluator = BoolArrayEvaluator()
        p3engine.run(config)
