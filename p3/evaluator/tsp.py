# -*- coding: utf-8 -*-

'''
TSP problem evaluator.
'''

import sys


class TSPEvaluator(object):

    def __init__(self, path):

        self._tsp_distances = []

        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                row = [int(x) for x in line.rstrip().split(' ') if x]
                self._tsp_distances.append(row)

    def evaluate(self, genotype):

        cost = 0
        length = len(genotype)
        unique = set()

        for i, item in enumerate(genotype):

            if item in unique:
                return -sys.maxsize

            if i + 1 == length:
                next_item = 0
            else:
                next_item = genotype[i + 1]

            unique.add(item)

            cost += self._tsp_distances[item][next_item]

        return -cost
