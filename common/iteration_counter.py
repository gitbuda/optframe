#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging
from helpers.setter import setter
from common.exception.limit_exception import LimitException

log = logging.getLogger(__name__)


class IterationCounter(object):

    def __init__(self):
        '''
        '''
        self.iteration = 0

    def configure(self, config=None):
        '''
        '''
        self.iteration_limit = setter(
            lambda: int(config.iteration_limit), None)

    def increase(self):
        '''
        '''
        self.iteration += 1

        if self.iteration_limit is not None \
           and self.iteration > self.iteration_limit:
            raise LimitException('Iteration limit is reached')


if __name__ == '__main__':
    pass
