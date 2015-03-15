# -*- coding: utf-8 -*-

'''
Binary array genotype
e.g.
[1, 0, 1, 0, 0, 1, 1, ...]
'''

import numpy
import copy


class BitArrayGenotype(object):

    def __init__(self, genotype_size):
        self.genotype_size = genotype_size
        self.genotype = numpy.random.randint(0, 2, self.genotype_size)

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
