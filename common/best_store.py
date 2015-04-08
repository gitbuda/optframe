#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Storage for the best solution and the best fitness.
'''

import sys
import logging

log = logging.getLogger(__name__)


class BestStore(object):

    def __init__(self):

        self.best_fitness = -sys.maxsize
        self.best_solution = None

    def try_store(self, fitness, solution):
        '''
            if fitness is better than the best fitness until
            now update the best fitness and the best solution
        '''

        if self.best_fitness < fitness:
            self.best_fitness = fitness
            self.best_solution = solution

            log.info('Best solution until now has fitness: %s' %
                     fitness)
