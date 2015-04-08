# -*- coding: utf-8 -*-

'''
MAX SAT problem evaluator.
'''

import random
import logging

from common.evaluation_counter import EvaluationCounter

log = logging.getLogger(__name__)


class Config(object):
    '''
    '''
    def __init__(self):
        self.solution_size = 20
        self.clause_size = 3
        self.clause_number = 10


class Evaluator(object):

    def __init__(self):
        '''
        '''
        self.evaluation_counter = EvaluationCounter()

    def configure(self, config=''):
        '''
        '''
        self.evaluation_counter.configure(config)

        self.solution_size = int(config.solution_size)
        self.clause_size = int(config.clause_size)
        self.clause_number = int(config.clause_number)
        self.clauses = []
        self.signs = []

        literals = [i for i in range(self.solution_size)]
        for i in range(self.clause_number):
            random.shuffle(literals)
            self.clauses.append(literals[:self.clause_size])
            while True:
                signs = [random.randint(0, 1) for x in range(self.clause_size)]
                if sum(signs) > 0:
                    self.signs.append(signs)
                    break

    def evaluate(self, solution):
        '''
        '''
        self.evaluation_counter.increment()

        fitness = 0
        for i in range(self.clause_number):
            for c in range(self.clause_size):
                if solution[self.clauses[i][c]] == self.signs[i][c]:
                    fitness += 1
                    break

        return fitness


if __name__ == '__main__':

    evaluator = Evaluator()
    config = Config()
    evaluator.configure(config)
    solution = [random.randint(0, 1) for x in range(evaluator.solution_size)]
    print evaluator.clauses
    print evaluator.signs
    print solution
    print evaluator.evaluate(solution)
