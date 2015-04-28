#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
PBOA config
'''

import logging

log = logging.getLogger(__name__)


class Config(object):

    def __init__(self):
        log.info('PBOA config')

    def load_problem_conf(self, problem_config):
        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):
        self.config.weak_merge(algorithm_config)

        # e.g.
        self.solution_size = int(self.config.solution_size)


if __name__ == '__main__':
    pass
