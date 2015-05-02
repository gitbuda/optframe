#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A problem solution.

Elements:
    container: solution elements, collection of
    box objects
    fitness: solution quality, instance of Fitness class
'''

import copy
import logging


log = logging.getLogger(__name__)


class Solution(object):

    def __init__(self, container, fitness=None):
        '''
        Args:
            container: solution elements (dict object)
            fitness: solution fitness
        '''
        self.container = container
        self.fitness = fitness

    def create_tuple(self):
        '''
        All box (elements of container) concatenated
        together in a large toupe object so it can be
        added to a set.
        '''
        all_values = []
        for key, value in self.container.items():
            all_values.extend(value)
        return tuple(all_values)

    def deep_copy(self):
        '''
        Deep copy of the object.
        '''
        return copy.deepcopy(self)


if __name__ == '__main__':

    s = Solution({"bit": [0, 1, 0, 1], "permutation": [2, 3, 4, 0, 1]})
    sc = s.deep_copy()
    sc.container['bit'][0] = 1
    sc.container['permutation'][1] = -1
    print s.container
    print sc.container
