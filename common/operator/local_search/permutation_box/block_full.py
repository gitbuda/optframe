#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging
from itertools import permutations
from common.constants import PERMUTATION_BOX_KEY
from helpers.setter import setter

log = logging.getLogger(__name__)


class LocalSearch(object):

    def __init__(self):
        '''
        '''
        pass

    def configure(self, context):
        '''
        '''
        self.evaluator = context.evaluate_operator
        self.block_size = setter(
            lambda: int(context.config.permutation.block_size), 2)

    def search(self, solution):
        '''
        '''
        block_size = self.block_size
        genotype = solution.container[PERMUTATION_BOX_KEY]
        genotype_size = len(genotype)
        block_counter = 0
        blocks = []
        for i in range(genotype_size):
            if i % block_size == 0 and i != 0:
                block_counter += 1
                block = genotype[i-block_size:i]
                blocks.append(list(block))
            if i == genotype_size - 1:
                block = genotype[block_counter*block_size:]
                blocks.append(list(block))
        best_fitness = solution.fitness
        for i, item in enumerate(blocks):
            perms = permutations(item)
            for k, perm in enumerate(perms):
                new_solution = []
                for j, block in enumerate(blocks):
                    if i == j:
                        new_solution += list(perm)
                    else:
                        new_solution += list(block)
                solution.container[PERMUTATION_BOX_KEY] = new_solution
                tmp_fitness = self.evaluator.evaluate(solution)
                if tmp_fitness > best_fitness:
                    best_fitness = tmp_fitness
                    solution.fitness = tmp_fitness
                else:
                    solution.container[PERMUTATION_BOX_KEY] = genotype

        return solution


if __name__ == '__main__':
    pass
