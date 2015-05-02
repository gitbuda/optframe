#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Linkage Tree Genetic Algorithm Context
'''

import logging
from common.best_store import BestStore
from common.iteration_counter import IterationCounter
from common.operator.collection.operator import Operator as CollectionOperator

log = logging.getLogger(__name__)


# TODO: rename in Context
class Config(object):

    def __init__(self):
        '''
        '''
        log.info('LTGA context setup start...')

    def load_problem_conf(self, problem_config):
        '''
        '''
        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):
        '''
        '''
        self.config.weak_merge(algorithm_config)

        # parameters
        self.solution_structure = self.config.solution_structure

        # operators
        self.best_store = BestStore()
        self.best_store.configure(self.config)

        self.iteration_counter = IterationCounter()
        self.iteration_counter.configure(self.config)

        self.collection_operator = CollectionOperator()
        self.collection_operator.configure(self.config)

        log.info('LTGA context setup end.')


if __name__ == '__main__':
    pass
