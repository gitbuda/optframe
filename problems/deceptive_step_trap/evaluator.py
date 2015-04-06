# -*- coding: utf-8 -*-

'''
Deceptive step trap problem evaluator.
'''

import logging

log = logging.getLogger(__name__)


class Config(object):
    def __init__(self):
        self.trap_size = 7
        self.step_size = 2


class Evaluator(object):

    def __init__(self):
        self.evaluations_number = 0

    def configure(self, config=''):
        self.trap_size = int(config.trap_size)
        self.step_size = int(config.step_size)
        self.offset = (self.trap_size - self.step_size) % self.step_size
        self.trap_max = (self.offset + self.trap_size) / self.step_size

    def evaluate(self, solution):
        self.evaluations_number += 1

        total = 0
        for i in xrange(0, len(solution), self.trap_size):
            partial = 0
            trap_end_i = i + self.trap_size
            if trap_end_i > len(solution):
                trap_end_i = len(solution)
            for index in xrange(i, trap_end_i):
                partial += solution[index]
            if partial < self.trap_size:
                partial = self.trap_size - partial - 1
            total += (self.offset + partial) / self.step_size
        return total


if __name__ == '__main__':

    evaluator = Evaluator()
    config = Config()
    evaluator.configure(config)
    print evaluator.evaluate([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
