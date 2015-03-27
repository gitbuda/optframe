# -*- coding: utf-8 -*-

'''
PGAConfig
'''

import logging
log = logging.getLogger(__name__)


class Config(object):

    def __init__(self):
        self.parameters = {}

    def load_problem_conf(self, problem_config):
        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):

        self.config.weak_merge(algorithm_config)

        self.mutation_factor = float(self.config.mutation_factor)
        self.crossover_factor = float(self.config.crossover_factor)
        self.solution_number = int(self.config.solution_number)

        log.info('PGA configuration loaded.')
