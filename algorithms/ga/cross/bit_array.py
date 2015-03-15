#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Framework specific standard float cross operator.
'''

import random


class BitArrayCrossOperator(object):

    def __init__(self):
        pass

    def cross(self, genotype_better, genotype_worse):
        '''
        '''

        new_genotype = list(genotype_better)
        genotype_size = len(genotype_better)

        for i, gene_better in enumerate(new_genotype):

            points = [random.randint(0, genotype_size - 1),
                      random.randint(0, genotype_size - 1)]
            points.sort()

            new_genotype = genotype_better[0:points[0]] + \
                genotype_worse[points[0]:points[1]] + \
                genotype_better[points[1]:-1]

        return new_genotype
