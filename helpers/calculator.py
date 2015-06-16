# -*- coding: utf-8 -*-

'''
Math helper class.
'''

import math


def neg_entropy(counts, total):
    '''
    Calculates negative entropy of counts array.

    Args:
        counts: array of frequncies
        total:  sum of all elements in counts
    '''
    sum_all = 0
    for value in counts:
        if value:
            p = float(value) / total
            sum_all += p * math.log(p, 2)
    return sum_all


def float_round(value, precision):
    '''
    Round the float value with some precision.

    Args:
        value:     float value
        precision: round precision
    '''
    return 1.0 * round(value * precision) / precision
