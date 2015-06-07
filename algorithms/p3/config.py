# -*- coding: utf-8 -*-

'''
P3 Config
'''

import logging
from common.best_store import BestStore
from common.iteration_counter import IterationCounter
from common.operator.collection.operator import Operator as CollectionOperator
from common.operator.local_search.operator import Operator as LocalSearch
from common.operator.cluster_cross.operator import Operator as ClusterCross

log = logging.getLogger(__name__)


class Config(object):

    def __init__(self):

        log.info('P3 Config Init')

    def load_problem_conf(self, problem_config):

        log.info('P3 Config Start')

        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):

        self.config.weak_merge(algorithm_config)

        print self.config

        # parameters
        self.solution_number = int(self.config.solution_number)
        self.solution_structure = self.config.solution_structure
        self.output_dir = self.config.output_path

        # operators
        self.best_store = BestStore()
        self.best_store.configure(self.config)

        self.iteration_counter = IterationCounter()
        self.iteration_counter.configure(self.config)

        self.collection_operator = CollectionOperator()
        self.collection_operator.configure(self.config)

        self.local_search = LocalSearch()
        self.local_search.configure(self)

        self.cluster_cross = ClusterCross()
        self.cluster_cross.configure(self)

        log.info('P3 Config End')
