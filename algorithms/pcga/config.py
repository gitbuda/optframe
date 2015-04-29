#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
PCGA config
'''

import logging

log = logging.getLogger(__name__)


class Config(object):

    def __init__(self):
        '''
        '''
        log.info('PCGA config')

    def load_problem_conf(self, problem_config):
        '''
        Load problem config (problem specific configuration
        items).

        Args:
            problem_config: configuration items, some kind of
            key value store
        '''
        self.config = problem_config

    def load_algorithm_conf(self, algorithm_config):
        '''
        Load algorithm config (algorighm specific configuration\
        items) and prepare all parameters for algorithm execution.
        '''
        # here is weak_merge because problem specific configuration
        # items has higher priority than algorithm configuration\
        # items
        self.config.weak_merge(algorithm_config)
        
        # PCGA algorithm only has to know solutution size in order
        # to generate new solutions.
        self.solution_size = int(self.config.solution_size)


if __name__ == '__main__':
    pass
