# -*- coding: utf-8 -*-

'''
BOA config
'''

import logging

log = logging.getLogger(__name__)


class Config(object):

    def __init__(self):

        log.info('BOA Config Init')

    def load_problem_conf(self, problem_config):

        log.info('BOA Config Start')

        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):

        self.config.weak_merge(algorithm_config)

        print self.config

        # setup parameters
        self.solution_size = int(self.config.solution_size)
        self.iterations_number = int(self.config.iterations_number)
        self.population_size = int(self.config.population_size)
        self.select_size = self.population_size / 2
        self.childern_number = self.population_size / 2

        log.info('BOA Config End')
