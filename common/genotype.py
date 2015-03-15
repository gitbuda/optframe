# -*- coding: utf-8 -*-

'''
Genotype -> array + fitness
'''

import copy


class Genotype(object):

    def __init__(self, genotype=None, fitness=None):
        self.genotype = genotype
        self.fitness = fitness

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
