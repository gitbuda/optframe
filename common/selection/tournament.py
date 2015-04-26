#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import random
import logging

from common.solution import Solution

log = logging.getLogger(__name__)


class Tournament(object):
    '''
    '''
    def __init__(self, k=3):
        '''
        '''
        self.k = k

    def select(self, population):
        '''
        '''
        size = len(population)
        if size < self.k:
            selected = sorted(population, key=lambda x: x.fitness,
                              reverse=True)
        else:
            randoms = random.sample(xrange(size), self.k)
            selected = []
            for index in randoms:
                selected.append(population[index])
            selected = sorted(selected, key=lambda x: x.fitness, reverse=True)

        return selected[0]

if __name__ == '__main__':

    population = [Solution(100, 100), Solution(200, 200), Solution(300, 300),
                  Solution(50, 50)]
    t = Tournament()
    solution = t.select(population)
    print solution.fitness
    print solution.box
