#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A problem solution.
'''

import logging

log = logging.getLogger(__name__)


class Solution(object):

    def __init__(self, box=None, fitness=None):
        '''
        Args:
            box: solution elements, this could be
                 a vector on let say a dict, problem or algorithm
                 define what kind of object is box
            fitness: solution fitness
        '''
        self.box = box
        self.fitness = fitness


if __name__ == '__main__':
    pass
