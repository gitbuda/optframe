#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Linkage Tree Population
'''

import logging
import common.constants as CONST
from collections import defaultdict
from common.clustering import upgma
from helpers.calculator import neg_entropy

log = logging.getLogger(__name__)

# TODO: different type of clustering


class LTPopulation:

    def __init__(self, solution_structure):
        '''
        Args:
            solution_structure
        '''

        self.solution_structure = solution_structure
        self.solutions = []
        self.reset_calculations()

    def configure(self, config):
        '''
        '''
        # TODO: clustering configuration
        pass

    def reset_calculations(self):
        '''
        '''
        self.occurrences = {}
        self.pairwise_distance = {}
        self.clusters = {}
        for key in self.solution_structure.keys():
            size = int(self.solution_structure[key].size)
            self.occurrences[key] = defaultdict(lambda: defaultdict(list))
            self.pairwise_distance[key] = [[0.0 for x in range(size)]
                                           for x in range(size)]

    def recalculate_for(self, solution, key, values_no):
        '''
        '''
        genotype = solution.container[key]
        for i in range(len(genotype) - 1):
            for j in range(i + 1, len(genotype)):
                if not self.occurrences[key][i][j]:
                    self.occurrences[key][i][j] = [0] * values_no**2
                entry = self.occurrences[key][i][j]
                index = genotype[j] * values_no + genotype[i]
                entry[index] += 1
                self.update_entropy(i, j, entry, key, values_no)

    def recalculate_solution(self, solution, rebuild_tree=True):
        '''
        '''
        for key in self.solution_structure.keys():
            if key == CONST.BIT_BOX_KEY:
                values_no = 2
            if key == CONST.PERMUTATION_BOX_KEY:
                values_no = int(self.solution_structure.permutation.size)
            if key == CONST.INT_BOX_KEY:
                values_no = int(self.solution_structure.int.max) - \
                    int(self.solution_structure.int.min) + 1
            self.recalculate_for(solution, key, values_no)

        if rebuild_tree:
            self.rebuild_tree()

    def add(self, solution, rebuild_tree=True):
        '''
        '''
        self.solutions.append(solution)
        self.recalculate_solution(solution, rebuild_tree)

    def recalculate_population(self):
        '''
        Reset calculations and rebuild tree.
        Only one cluster operation.
        '''
        self.reset_calculations()
        for solution in self.solutions:
            self.recalculate_solution(solution, False)
        self.rebuild_tree()

    def update_entropy(self, i, j, entry, key, values_no):
        '''
        '''
        total_size = values_no * 2
        bits = [0] * total_size
        for k in range(values_no):
            for l in range(values_no):
                bits[k] += entry[k + l * values_no]
        for k in range(values_no):
            for l in range(values_no):
                bits[values_no + k] += entry[k * values_no + l]
        total = sum(entry)
        separate = neg_entropy(bits, total)
        together = neg_entropy(entry, total)
        ratio = float(0)
        if together:
            ratio = 2 - (separate / together)
        self.pairwise_distance[key][i][j] = ratio
        self.pairwise_distance[key][j][i] = ratio

    def rebuild_tree(self):
        '''
        '''
        for key in self.solution_structure.keys():
            self.clusters[key] = upgma.build(self.pairwise_distance[key])


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
