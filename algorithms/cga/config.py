#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Compact Genetic Algorithm config
'''

import logging

log = logging.getLogger(__name__)


class Config(object):

    def __init__(self):
        log.info('CGA Config')

    def load_problem_conf(self, problem_config):
        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):
        self.config.weak_merge(algorithm_config)

        self.solution_size = int(self.config.solution_size)
        self.population_size = int(self.config.population_size)
        self.iterations_number = int(self.config.iterations_number)


if __name__ == '__main__':
    pass
