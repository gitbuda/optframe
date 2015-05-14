# -*- coding: utf-8 -*-

'''
PGAConfig
'''

import logging
from helpers.setter import setter
from common.selection.tournament import Selection
from common.operator.collection.operator import Operator as PopulationOperator
from common.operator.cross_operator import CrossOperator
from common.operator.mutation_operator import MutationOperator
from common.operator.local_search.operator import Operator as LocalSearch

log = logging.getLogger(__name__)


class Config(object):

    def __init__(self):
        self.parameters = {}

    def load_problem_conf(self, problem_config):
        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):

        self.config.weak_merge(algorithm_config)

        self.mutation_factor = float(self.config.mutation_factor)
        self.cross_factor = float(self.config.cross_factor)
        self.solution_number = setter(
            lambda: int(self.config.solution_number), 200)

        self.init_solution_operator = PopulationOperator()
        self.init_solution_operator.configure(self.config)

        self.mutation_operator = MutationOperator()
        self.mutation_operator.configure(self.config)

        self.cross_operator = CrossOperator()
        self.cross_operator.configure(self.config)

        self.local_search = LocalSearch()
        self.local_search.configure(self)

        self.selection_operator = Selection()

        log.info('PGA configuration loaded.')
