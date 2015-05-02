#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
CVP - Compact Probability Vector
'''

import random
import logging

from common.solution import Solution
from common.constants import BIT_BOX_KEY

log = logging.getLogger(__name__)


class CompactProbabilityVector(object):

    def __init__(self, solution_size):
        self.size = solution_size
        self.vector = [0.5 for x in xrange(self.size)]

    def generate_candidate(self):
        '''
        '''
        candidate = Solution({BIT_BOX_KEY: [0 for x in xrange(self.size)]})
        for i, p in enumerate(self.vector):
            gene = 1 if random.random() < p else 0
            candidate.container[BIT_BOX_KEY][i] = gene
        return candidate

    def update_vector(self, winner, loser, population_size):
        '''
        '''
        for i in xrange(len(self.vector)):
            winner_bit = winner.container[BIT_BOX_KEY][i]
            loser_bit = loser.container[BIT_BOX_KEY][i]
            if winner_bit != loser_bit:
                if winner_bit == 1:
                    self.vector[i] += 1.0 / population_size
                else:
                    self.vector[i] -= 1.0 / population_size

                # if value goes out of the scope
                # put it back to the initial value
                # because if population size is small then
                # the value easily can wrong value
                if self.vector[i] < 0 or self.vector[i] > 1:
                    self.vector[i] = 0.5


if __name__ == '__main__':
    pass
