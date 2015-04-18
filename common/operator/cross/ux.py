#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Implementation of UX cross operator.
'''

import random


class UXCrossOperator(object):

    def __init__(self, cross_factor):
        '''
        '''
        self.cross_factor = cross_factor

    def cross(self, genotype_better, genotype_worse):
        '''
        '''
        length = len(genotype_better)

        # make copy of genotype
        new_genotype = list(genotype_worse)

        for i in range(length):
            decision = random.random()
            if decision < self.cross_factor:
                new_genotype[i] = genotype_better[i]

        return new_genotype


if __name__ == '__main__':

    operator = UXCrossOperator(0.5)

    first = ['B', 'A', 'C', 'D', 'E', 'F', 'G', 'H']
    second = ['E', 'G', 'A', 'C', 'B', 'F', 'D', 'H']

    first = ['B', 'A', 'C', 'D', 'E', 'F', 'G', 'H']
    second = ['E', 'G', 'A', 'C', 'D', 'F', 'B', 'H']

    first = [1, 2, 3, 4]
    second = [5, 6, 8, 7]

    print first
    print second
    print ""
    print operator.cross(first, second)
