#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Run P3 algorithm.
'''

import logging
from p3 import p3engine
from p3config import P3Config


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    config = P3Config()
    p3engine.run(config)
