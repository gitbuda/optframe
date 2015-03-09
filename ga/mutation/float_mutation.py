#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Standard float mutation operator.
This operator iterates through genes and
with propabilty of mutataion factor set
a genes to random float number between 0 and 1. 
'''

import random


class FloatMutation(object):

    def __init__(self, mutation_factor):
        self._mutation_factor = mutation_factor

    @property
    def mutation_factor(self):
        return self._mutation_factor

    def mutate(self, genes):

        for i, gene in enumerate(genes):
            random_float = random.random()
            if random_float < self.mutation_factor:
                genes[i] = random.random()


if __name__ == '__main__':

    operator = FloatMutation(0.1)

    genotype = [random.random() for i in range(20)]

    old_genotype = list(genotype)

    operator.mutate(genotype)

    for x, y in zip(old_genotype, genotype):
        print '%s %s' % (x, y)
