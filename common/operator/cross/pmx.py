#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Implementation of PMX cross operator.
'''

import random


class PMXCrossOperator(object):

    def __init__(self):
        pass

    def cross(self, genotype_better, genotype_worse):

        # get genotype length
        length = len(genotype_better)

        # make copy of genotype
        new_genotype = list(genotype_better)

        # get two points for crossover
        # random, different and sorted
        random_pair = set()
        while len(random_pair) < 2:
            random_pair.add(random.randint(0, length))
        random_pair = sorted(list(random_pair))
        first = random_pair[0]
        second = random_pair[1]

        # swap part of arrays
        # build pmx_map
        # build not allowed set
        tmp_better = genotype_worse[first:second]
        tmp_worse = genotype_better[first:second]
        new_genotype[first:second] = genotype_worse[first:second]
        pmx_map = {}
        for i in range(second - first):
            pmx_map[tmp_better[i]] = tmp_worse[i]
        not_allowed = set(tmp_better)

        # use pmx_map to fill solution
        # try to replace gen from new_genotype with pmx_map
        # but item for replacement may not be in not_allowed set
        # applay this to first and last part of the array
        for i in range(0, first):
            if new_genotype[i] in pmx_map:
                candidate = pmx_map[new_genotype[i]]
                while candidate in not_allowed:
                    candidate = pmx_map[candidate]
                new_genotype[i] = candidate
        for i in range(second, length):
            if new_genotype[i] in pmx_map:
                candidate = pmx_map[new_genotype[i]]
                while candidate in not_allowed:
                    candidate = pmx_map[candidate]
                new_genotype[i] = candidate

        return new_genotype

if __name__ == '__main__':

    operator = PMXCrossOperator()

    # first = ['B', 'A', 'C', 'D', 'E', 'F', 'G', 'H']
    # second = ['E', 'G', 'A', 'C', 'B', 'F', 'D', 'H']

    first = ['B', 'A', 'C', 'D', 'E', 'F', 'G', 'H']
    second = ['E', 'G', 'A', 'C', 'D', 'F', 'B', 'H']

    print first
    print second
    print ""
    print operator.cross(first, second)
