# -*- coding: utf-8 -*-

'''
TSP problem evaluator.
'''

import sys


class Evaluator(object):

    def __init__(self):
        pass

    def configure(self, config=''):

        path = config.input_file_path
        self._tsp_distances = []

        with open(path) as f:
            lines = iter(f.readlines())
            for line in lines:
                if 'DIMENSION:' in line:
                    dimension = int(line.split(':')[1])
                if 'EDGE_WEIGHT_SECTION' in line:
                    break
            for weight_index in xrange(dimension):
                line = lines.next()
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
