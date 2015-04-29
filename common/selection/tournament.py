#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
k-tournament selection operator.
'''

import random
import logging

from common.solution import Solution

log = logging.getLogger(__name__)


class Selection(object):

    def __init__(self, k=3):
        '''
        Tournament size initializator.

        Args:
            k: tournament size
        '''
        self.k = k

    def select(self, population, n=1):
        '''
        Select n solutions from population.

        Args:
            population: selection pool
            n: selection size, first k elements are taken into
               the tournament and than the best n are returned
        '''
        size = len(population)

        # if population size < k then take the best elements from
        # whole population
        if size < self.k:
            selected = sorted(population, key=lambda x: x.fitness,
                              reverse=True)
        else:
            randoms = random.sample(xrange(size), self.k)
            selected = []
            for index in randoms:
                selected.append(population[index])
            selected = sorted(selected, key=lambda x: x.fitness, reverse=True)

        return selected[0:n]


if __name__ == '__main__':

    population = [Solution(100, 100), Solution(200, 200), Solution(300, 300),
                  Solution(50, 50)]
    t = Selection()
    solution = t.select(population)
    print solution.fitness
    print solution.box
