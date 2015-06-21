#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Storage for the best solution and the best fitness.
Fitness is element of the solution.
'''

import logging

from helpers.setter import setter
from common.solution import Solution
from common.exception.limit_exception import LimitException
from common.fitness import Fitness, MIN, MAX, MIN_NAME, MAX_NAME

log = logging.getLogger(__name__)


class BestStore(object):

    def __init__(self):
        '''
        '''
        self.best_solution = None
        self.best_config = None
        self.fitness_limit = None

    def best(self, evaluator=None):
        # TODO: remove evaluator from here
        # inject an evaluator via configuration method
        # evaluator has to be injected because only it knows
        # to return the worst solution
        if self.best_solution:
            return self.best_solution
        else:
            if evaluator:
                return Solution({}, evaluator.theworst_fitness())
            else:
                return Solution({})

    def configure(self, config=None):
        '''
        '''
        # setup fitness limit
        # TODO: too complex refactor
        fitness_limit_value = setter(
            lambda: float(config.fitness_limit.value), None)
        fitness_limit_category_name = setter(
            lambda: config.fitness_limit.category, None)
        if fitness_limit_value is not None and \
           fitness_limit_category_name is not None:
            if fitness_limit_category_name == MIN_NAME:
                self.fitness_limit = Fitness(fitness_limit_value, MIN)
            elif fitness_limit_category_name == MAX_NAME:
                self.fitness_limit = Fitness(fitness_limit_value, MAX)

    def try_store(self, solution, config=None):
        '''
        if fitness is better than the best fitness until
        now update the best solution and the best configuration
        '''
        if self.best_solution is None or \
           self.best_solution.fitness < solution.fitness:
            self.best_solution = solution
            self.best_config = config
            log.info('Best solution is now: %s' % solution.container)
            log.info('Best solution has now fitness: %s' %
                     (solution.fitness.value))

            if self.fitness_limit is not None and \
               self.best_solution.fitness >= self.fitness_limit:
                raise LimitException('Fitness limit reached')
