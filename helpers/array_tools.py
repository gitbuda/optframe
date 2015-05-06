#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import random
import logging

log = logging.getLogger(__name__)


def swap(a, b, ind):
    '''
    The function swap elements of a and b
    on indices stored in ind.

    Args:
        a: list of elements
        b: list of elements
        ind: list indices
    '''
    for i in ind:
        a[i], b[i] = b[i], a[i]

def permutation_swap(a, b, ind):
    '''
    The function swap elements of a and b on
    indiecs stored in ind,
    but it takes care that after swap
    a and b stay permutations.

    Args:
        a: list of elements
        b: list of elements
        ind: list indices
    '''
    used_a = set()
    used_b = set()
    candidates_a = set()
    candidates_b = set()
    for i in ind:
        used_a.add(b[i])
        used_b.add(a[i])
        a[i], b[i] = b[i], a[i]

    used = set()
    for i in xrange(len(a)):
        if a[i] in used_a:
            candidates_a = used_b.difference(used_a).difference(set([a[i]])).difference(used)
            if len(candidates_a):
                element = random.sample(candidates_a, 1)[0]
                a[i] = element
                used.add(element)
    used = set()
    for i in xrange(len(b)):
        if b[i] in used_b:
            candidates_b = used_a.difference(used_b).difference(set([b[i]])).difference(used)
            if len(candidates_b):
                element = random.sample(candidates_b, 1)[0]
                b[i] = element
                used.add(element)



if __name__ == '__main__':

    array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print "normal swap"
    print array1, array2
    swap(array1, array2, [0, 1, 5])
    print array1, array2
    array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print "permutation swap"
    print array1, array2
    permutation_swap(array1, array2, [0, 1, 5])
    print array1, array2
