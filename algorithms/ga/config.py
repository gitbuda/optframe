#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.selection.tournament import Selection
from common.operator.collection.operator import Operator as PopulationOperator
from common.operator.cross_operator import CrossOperator
from common.operator.mutation_operator import MutationOperator

from algorithms.ga.termination.termination import max_iteration


class Config(object):
    '''
        TODO: read all from conf file
    '''
    def __init__(self):
        self.parameters = {}

    def load_problem_conf(self, problem_config):
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

        self.termination_operator = max_iteration

        self.mutation_operator = MutationOperator()
        self.mutation_operator.configure(self.config)

        self.cross_operator = CrossOperator()
        self.cross_operator.configure(self.config)

        self.selection_operator = Selection()


if __name__ == '__main__':
    pass
