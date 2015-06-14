#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from problems.cvrp.greedy1 import Greedy as Greedy1
from problems.cvrp.greedy2 import Greedy as Greedy2


class SolutionOperator(object):

    def __init__(self):
        pass

    def configure(self, config):
        self.greedy_pool = []
        self.greedy_pool.append(Greedy1().configure(config))
        self.greedy_pool.append(Greedy2().configure(config))
        return self

    def next(self):
        rand = random.randint(0, len(self.greedy_pool) - 1)
        return self.greedy_pool[rand].run()


if __name__ == '__main__':

    from helpers.dict_wrapper import DictWrapper
    from problems.cvrp.evaluator import Evaluator

    print 'CVRP solution operator manual test'

    config = DictWrapper({'path': 'input.txt', 'warehouses': [2, 4, 5]})
    operator = SolutionOperator().configure(config)
    evaluator = Evaluator().configure(config)

    solution = operator.next()
    fitness = evaluator.evaluate(solution)
    solution.fitness = fitness

    print solution
    solution.persist('output/example.txt')
