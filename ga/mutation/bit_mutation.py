#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Standard bit mutation operator.
This operator iterates through genes and
with propabilty of mutataion factor set
a genes to inverted gene value.
'''

import random


class BitMutationOperator(object):

    def __init__(self, mutation_factor):
        self._mutation_factor = mutation_factor

    @property
    def mutation_factor(self):
        return self._mutation_factor

    def mutate(self, genes):

        for i, gene in enumerate(genes):
            random_float = random.random()
            if random_float < self.mutation_factor:
                if genes[i] == 1:
                    genes[i] = 0
                else:
                    genes[i] = 1
