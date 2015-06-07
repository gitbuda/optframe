# -*- coding: utf-8 -*-

'''
Genetic Algorithm Config
'''

import logging
from common.best_store import BestStore
from common.selection.tournament import Selection
from common.operator.collection.operator import Operator as PopulationOperator
from common.operator.cross_operator import CrossOperator
from common.operator.mutation_operator import MutationOperator
from common.iteration_counter import IterationCounter

log = logging.getLogger(__name__)


class Config(object):

    def __init__(self):

        log.info('GA Init')

    def load_problem_conf(self, problem_config):

        log.info('GA Config Start')

        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):

        self.config.weak_merge(algorithm_config)

        print self.config

        # define all parameters
        self.population_size = int(self.config.population_size)
        self.max_iterations = int(self.config.iterations_number)
        self.best_to_next_number = int(self.config.best_to_next_number)

        # load all operators
        self.population_operator = PopulationOperator()
        self.population_operator.configure(self.config)

        self.mutation_operator = MutationOperator()
        self.mutation_operator.configure(self.config)

        self.cross_operator = CrossOperator()
        self.cross_operator.configure(self.config)

        self.selection_operator = Selection()

        self.best_store = BestStore()
        self.best_store.configure(self.config)

        self.iteration_counter = IterationCounter()
        self.iteration_counter.configure(self.config)

        log.info('GA Config End')
