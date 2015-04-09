#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from algorithms.ga.optimization.structure.population import Population
from algorithms.ga.optimization.structure.genotype import Genotype


class PermutationPopulationOperator:

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
            genes = [x for x in range(self.genotype_size)]
            random.shuffle(genes)
            genotype.genes = genes
            population.append(genotype)

        return population
