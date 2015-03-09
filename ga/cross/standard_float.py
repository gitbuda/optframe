#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Framework specific standard float cross operator.
'''

import random


class StandardFloatCrossOperator(object):

    def __init__(self):
        pass

    def cross(genotype_better, genotype_worse):
        '''
        Iterates through genotypes and construct new genotype
        75% from the better genotype and 25% from worse genotype
        TODO: replace 75% and 25% with config coeffs
        '''

        new_genotype = list(genotype_better)

        for i, gene_better in enumerate(new_genotype):

            random_float = random.random()

            # TODO: read coeffs from config file
            if random_float < 0.5:
                new_genotype[i] = (gene_better + genotype_worse[i]) / 2.0
            elif random_float >= 0.5 and random_float < 0.75:
                new_genotype[i] = genotype_worse[i]
            else:
                pass

        return new_genotype
