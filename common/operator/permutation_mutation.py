#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This operator iterates through genes and
with propabilty of mutataion_factor swap random genes.
'''

import random


class PermutationMutationOperator(object):

    def __init__(self, mutation_factor):
        '''
        '''
        self._mutation_factor = mutation_factor

    @property
    def mutation_factor(self):
        return self._mutation_factor

    def mutate(self, genes):
        '''
        '''
        size = len(genes)

        for x in range(size):
            random_float = random.random()
            if random_float < self.mutation_factor:
                i = random.randint(0, size - 1)
                j = random.randint(0, size - 1)
                genes[i], genes[j] = genes[j], genes[i]


if __name__ == '__main__':
    pmo = PermutationMutationOperator(0.5)
    genes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pmo.mutate(genes)
    print genes
