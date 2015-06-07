#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Linkage Tree Genetic Algorithm Config
'''

import logging
from common.best_store import BestStore
from common.iteration_counter import IterationCounter
from common.operator.collection.operator import Operator as CollectionOperator
from common.operator.local_search.operator import Operator as LocalSearch

log = logging.getLogger(__name__)


class Config(object):

    def __init__(self):

        log.info('LTGA Config Init')

    def load_problem_conf(self, problem_config):

        log.info('LTGA Config Start')

        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):

        self.config.weak_merge(algorithm_config)

        print self.config

        # parameters
        self.solution_structure = self.config.solution_structure

        # operators
        self.best_store = BestStore()
        self.best_store.configure(self.config)

        self.iteration_counter = IterationCounter()
        self.iteration_counter.configure(self.config)

        self.collection_operator = CollectionOperator()
        self.collection_operator.configure(self.config)

        self.local_search = LocalSearch()
        self.local_search.configure(self)

        log.info('LTGA Config End')
