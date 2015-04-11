#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Storage for the best solution and the best fitness.
For now only the fitness max is supported.
'''
# TODO: support for fitness min and fitness max

import sys
import logging

from helpers.loader import DictWrapper
from common.exception.termination_exception import TerminationException

log = logging.getLogger(__name__)


class BestStore(object):

    def __init__(self):
        '''
        '''
        self.best_fitness = -sys.maxsize
        self.best_solution = None

    def configure(self, config=DictWrapper()):
        '''
        '''
        try:
            self.best_fitness_constraint = float(config.best_fitness)
        except (KeyError, AttributeError):
            log.info('best fitness constraint none')
            self.best_fitness_constraint = None

    def try_store(self, fitness, solution):
        '''
        if fitness is better than the best fitness until
        now update the best fitness and the best solution
        '''
        if self.best_fitness < fitness:
            self.best_fitness = fitness
            self.best_solution = solution
            log.info('Best solution has now fitness: %s' % fitness)

            if self.best_fitness_constraint is not None and \
               self.best_fitness >= self.best_fitness_constraint:
                raise TerminationException()
