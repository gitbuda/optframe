#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import numpy as np
import logging
import copy


def swap(a, b, ind):
    copy_a = copy.copy(a)
    copy_b = copy.copy(b)
    elements_a = np.take(a, ind)
    np.put(copy_b, ind, elements_a)
    elements_b = np.take(b, ind)
    np.put(copy_a, ind, elements_b)
    return copy_a, copy_b

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
