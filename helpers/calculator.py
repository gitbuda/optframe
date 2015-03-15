#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import math
import logging


def neg_entropy(counts, total):
    sum_all = 0
    for value in counts:
        if value:
            p = float(value) / total
            sum_all += p * math.log(p, 2)
    return sum_all

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
