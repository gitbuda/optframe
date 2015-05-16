# -*- coding: utf-8 -*-

'''
Object which purpose is to store information about iteration
number. An algorithm define what is iteration and this object
stores iterations number and for every iteration the best
solution fitness, the last one property is called history
and isn't required.

Iteration counter could be configured with the iteration_limit
config property, when iteration counter reaches iteration_limit
it will raise Exception. If iteration_limit doesn't exist
iteration counter will never raise the Exception.
'''

import logging
from helpers.setter import setter
from common.exception.limit_exception import LimitException

log = logging.getLogger(__name__)


class IterationCounter(object):

    def __init__(self):
        '''
        Properties:
            iteration: number of iterations
            history: list of touples (iteration, Fitness)
        '''
        self.iteration = 0
        self.history = []

    def configure(self, config=None):
        '''
        Args:
            config: config.iteration_limit
        '''
        self.iteration_limit = setter(
            lambda: int(config.iteration_limit), None)

    def increase(self, solution=None):
        '''
        Update iteration and history.
        '''
        # update
        self.iteration += 1
        if solution is not None:
            self.history.append((self.iteration, solution.fitness))

        # only for debug purpose (it isn't for logger)
        if self.iteration % 1000 == 0:
            print 'iteration: %s' % str(self.iteration)

        # raise Exception if neccessary
        if self.iteration_limit is not None \
           and self.iteration > self.iteration_limit:
            raise LimitException('Iteration limit is reached')
