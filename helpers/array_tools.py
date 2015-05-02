#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

log = logging.getLogger(__name__)


def swap(a, b, ind):
    '''
    '''
    for i in ind:
        a[i], b[i] = b[i], a[i]


if __name__ == '__main__':

    array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print array1, array2
    swap(array1, array2, [0, 1, 5])
    print array1, array2
