#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
PBOA context
'''

import logging

from helpers.setter import setter
from common.iteration_counter import IterationCounter

log = logging.getLogger(__name__)


class Config(object):

    def __init__(self):
        '''
        '''
        log.info('PBOA context init')

    def load_problem_conf(self, problem_config):
        '''
        '''
        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):
        '''
        '''
        self.config.weak_merge(algorithm_config)

        # setup operators
        self.iteration_counter = IterationCounter()
        self.iteration_counter.configure(self.config)

        # parameters
        self.solution_size = int(self.config.solution_size)
        self.population_limit = setter(lambda: self.config.population_limit,
                                       50)
        self.childrens_number = setter(lambda: self.config.childrens_number,
                                       self.population_limit / 2)


if __name__ == '__main__':
    pass
