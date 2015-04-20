#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import random
import logging

from common.best_store import BestStore

log = logging.getLogger(__name__)


class Solution(object):
    def __init__(self, box=None, fitness=None):
        self.box = box
        self.fitness = None


def generate_candidate(vector, evaluator):
    '''
    '''
    candidate = Solution([0 for x in xrange(len(vector))])
    for i, p in enumerate(vector):
        gene = 1 if random.random() < p else 0
        candidate.box[i] = gene
    candidate.fitness = evaluator.evaluate(candidate.box)
    return candidate


def update_vector(vector, winner, loser, population_size):
    for i in xrange(len(vector)):
        if winner.box[i] != loser.box[i]:
            if winner.box[i] == 1:
                vector[i] += 1.0 / population_size
            else:
                vector[i] -= 1.0 / population_size


def run(context):
    '''
    '''
    # e.g.
    solution_size = context.solution_size
    population_size = context.population_size
    iterations_number = context.iterations_number
    evaluator = context.evaluate_operator

    best_store = BestStore()
    best_store.configure(context.config)

    try:
        vector = [0.5 for x in xrange(solution_size)]
        for iteration in xrange(iterations_number):
            c1 = generate_candidate(vector, evaluator)
            c2 = generate_candidate(vector, evaluator)
            winner, loser = (c1, c2) if c1.fitness > c2.fitness else (c2, c1)
            best_store.try_store(winner.fitness, winner)
            update_vector(vector, winner, loser, population_size)
    except Exception:
        pass

    return (best_store.best_solution, best_store.best_fitness)


if __name__ == '__main__':
    pass
