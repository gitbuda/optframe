#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

from collections import defaultdict
from common.clustering import upgma
from helpers.calculator import neg_entropy


log = logging.getLogger(__name__)


class LTPopulation:

    def __init__(self, size, values_no):

        self.size = size
        self.values_no = values_no
        self.solutions = []
        self.reset_calculations()

    def reset_calculations(self):
        self.occurrences = defaultdict(lambda: defaultdict(list))
        self.pairwise_distance = [[0.0 for x in range(self.size)]
                                  for x in range(self.size)]

    def recalculate_for(self, solution, rebuild_tree=True):
        genotype = solution.get_genotype()

        for i in range(len(solution.get_genotype()) - 1):
            for j in range(i + 1, len(solution.get_genotype())):
                if not self.occurrences[i][j]:
                    self.occurrences[i][j] = [0] * self.values_no**2
                entry = self.occurrences[i][j]
                index = genotype[j] * self.values_no + genotype[i]
                entry[index] += 1
                self.update_entropy(i, j, entry)

        if rebuild_tree:
            self.rebuild_tree()

    def add(self, solution, recalculate=True):
        self.solutions.append(solution)
        if recalculate:
            self.recalculate_for(solution, recalculate)

    def recalculate_population(self):
        self.reset_calculations()
        for solution in self.solutions:
            self.recalculate_for(solution, False)
        self.rebuild_tree()

    def update_entropy(self, i, j, entry):
        total_size = self.values_no * 2
        bits = [0] * total_size
        for k in range(self.values_no):
            for l in range(self.values_no):
                bits[k] += entry[k + l * self.values_no]
        for k in range(self.values_no):
            for l in range(self.values_no):
                bits[self.values_no + k] += entry[k * self.values_no + l]
        total = sum(entry)
        separate = neg_entropy(bits, total)
        together = neg_entropy(entry, total)
        ratio = float(0)
        if together:
            ratio = 2 - (separate / together)

        self.pairwise_distance[i][j] = ratio
        self.pairwise_distance[j][i] = ratio

    def rebuild_tree(self):
        self.clusters = upgma.build(self.pairwise_distance)

    def get_clusters(self):
        return self.clusters


if __name__ == '__main__':

    from algorithms.p3.genotype.bit_array import BitArrayGenotype
    import numpy as np

    def block_bit(size, block_size, index=-1):
        block = [0 for i in xrange(size)]
        if index == -1:
            return block
        start = block_size * index
        for i in xrange(start, start + block_size):
            block[i] = 1
        return np.array(block)

    # manual test
    size = 20
    block_size = 5
    lt_pop = LTPopulation(size, 2)
    solution = BitArrayGenotype(size)
    genotype = block_bit(size, block_size, 0)
    print genotype
    solution.set_genotype(genotype)
    lt_pop.add(solution)
    # genotype = block_bit(size, block_size, 1)
    # print genotype
    # solution.set_genotype(genotype)
    # lt_pop.add(solution)
    # genotype = block_bit(size, block_size, 2)
    # print genotype
    # solution.set_genotype(genotype)
    # lt_pop.add(solution)
    # genotype = block_bit(size, block_size, 0)
    # print genotype
    # solution.set_genotype(genotype)
    # lt_pop.add(solution)
    # solution.set_genotype(block_bit(size, block_size, 1))
    # lt_pop.add(solution)
