# -*- coding: utf-8 -*-

'''
Permutation genotype
e.g.
[0, 2, 1, 3, 4, 6, 5, 9, 8, 7]
'''

import numpy
import random
import copy


class PermutationGenotype(object):

    def __init__(self, genotype_size):
        self.genotype_size = genotype_size
        _genotype = [i for i in range(genotype_size)]
        random.shuffle(_genotype)
        self.genotype = numpy.array(_genotype)

    def get_genotype_size(self):
        return self.genotype_size

    def get_genotype(self):
        return self.genotype

    def get_fitness(self):
        return self.fitness

    def set_genotype(self, genotype):
        self.genotype = genotype

    def set_fitness(self, fitness):
        self.fitness = fitness

    def deep_copy(self):
        return copy.deepcopy(self)
