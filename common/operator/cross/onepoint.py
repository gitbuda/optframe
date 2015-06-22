#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Framework specific bit array cross operator.
'''

import random


class OnePointCrossOperator(object):

    def __init__(self, cross_factor):
        '''
        '''
        self.cross_factor = cross_factor

    def cross(self, genotype_better, genotype_worse):
        '''
        '''
        new_genotype = list(genotype_better)
        genotype_size = len(genotype_better)

        for i, gene_better in enumerate(new_genotype):

            point = random.randint(0, genotype_size - 1)

            new_genotype = genotype_better[0:point] + \
                genotype_worse[point:]

        # TODO: all cross operators have to return a touple
        return new_genotype
