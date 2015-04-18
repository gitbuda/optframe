#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Implementation of OX permutation cross operator
'''

import random


class OXCrossOperator(object):

    def __init__(self):
        '''
        '''
        pass

    def cross(self, genotype_better, genotype_worse):
        '''
        '''

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

        # already used elements
        not_allowed = set(new_genotype[first:second])
        # elements that have to be placed into new genotype
        for_import = genotype_worse[second:length] + genotype_worse[0:second]
        # ordered list of indices which has to
        for_populate = range(second, length) + range(0, first)

        # iterate throuth for_populate list
        # and pop elements from for_import
        # in order to fill new_genotype
        for i in for_populate:
            item = for_import.pop(0)
            while item in not_allowed:
                item = for_import.pop(0)
            new_genotype[i] = item

        return new_genotype


if __name__ == '__main__':

    operator = OXCrossOperator()

    first = ['B', 'A', 'C', 'D', 'E', 'F', 'G', 'H']
    second = ['E', 'G', 'A', 'C', 'B', 'F', 'D', 'H']

    first = ['B', 'A', 'C', 'D', 'E', 'F', 'G', 'H']
    second = ['E', 'G', 'A', 'C', 'D', 'F', 'B', 'H']

    first = [1, 2, 3, 5]
    second = [5, 2, 3, 1]

    print first
    print second
    print ""
    print operator.cross(first, second)
