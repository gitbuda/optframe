#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

from helpers.iniconfig import read

log = logging.getLogger(__name__)

SECTION = 'LTGA'
POPULATION_SIZE = 'PopulationSize'
ITERATIONS = 'Iterations'


class Config(object):

    def __init__(self):
        log.info('LTGA Config')

    def load_problem_conf(self, problem_config):
        self.problem_config = problem_config

    def load_algorithm_conf(self, path):
        self.settings = read(path)
        self.population_size = self.settings.getint(SECTION, POPULATION_SIZE)
        self.iterations = self.settings.getint(SECTION, ITERATIONS)


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
