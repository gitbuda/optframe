#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

from collections import defaultdict
from common.clustering import upgma
from helpers.calculator import neg_entropy


class LTPopulation:

    def __init__(self, size, values_no):

        self.size = size
        self.values_no = values_no
        self.solutions = []

        self.reset_calculations()

    def reset_calculations(self):
        self.occurrences = defaultdict(lambda: defaultdict(list))
        self.pairwise_distance = [[0] * self.size] * self.size
        self.clusters = [[]] * (2 * self.size - 1)

    def recalculate_for(self, solution, rebuild_tree=True):
        genotype = solution.get_genotype()

        for i in range(len(solution.get_genotype()) - 1):
            for j in range(i + 1, len(solution.get_genotype())):
                if not self.occurrences[i][j]:
                    self.occurrences[i][j] = [0] * \
                        self.values_no * self.values_no
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

    def get_distance(self, i, j):
        if (i > j):
            i, j = j, i
        return self.pairwise_distance[i][j]

    def rebuild_tree(self):
        (clusters, _) = upgma.build_clusters(self.pairwise_distance)
        self.clusters = clusters

    def get_clusters(self):
        return self.clusters

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
