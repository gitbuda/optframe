#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from ga.optimization.structure.population import Population
from ga.optimization.structure.genotype import Genotype


class BitArrayPopulationOperator:

    def __init__(self, size, genotype_size):
        self._size = size
        self._genotype_size = genotype_size

    @property
    def size(self):
        return self._size

    @property
    def genotype_size(self):
        return self._genotype_size

    def generate(self):

        population = Population()

        for i in range(self.size):
            genotype = Genotype()

            genotype.genes = [random.randint(0, 1)
                              for x in xrange(self.genotype_size)]

            population.append(genotype)

        return population
