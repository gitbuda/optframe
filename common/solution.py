#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A problem solution.

Elements:

    container: solution elements, collection of box objects
        e.g.
        container['bit'] = [1, 0, 1, 0, 0, ...]
        container['permutation'] = [3, 1, 2, 4, ...]
        container['float'] = [0.4, 0.32, ...]
        container['int'] = [1, 2, 2, 4, ...]

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

    def __str__(self):
        '''
        Solution string representation.
        '''
        string = ''
        string += '{\n'
        string += '  "fitness": %s,\n' % self.fitness.value
        for key, value in self.container.items():
            string += '  "%s": %s,\n' % (key, value)
        string = string[:-2]
        string += '\n}\n'
        return string

    def persist(self, destination):
        '''
        Save solution somewhere, for now only
        on the local file system.
        '''
        with open(destination, 'w') as f:
            f.write(str(self))


if __name__ == '__main__':
    from common.fitness import Fitness
    s = Solution({"bit": [0, 1, 0, 1], "permutation": [2, 3, 4, 0, 1]},
                 Fitness(323, 'min'))
    sc = s.deep_copy()
    sc.container['bit'][0] = 1
    sc.container['permutation'][1] = -1
    print s
    print sc
