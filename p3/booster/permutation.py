# -*- coding: utf-8 -*-

'''
Permutation Booster
'''

import numpy
from itertools import permutations


class PermutationBooster(object):

    def __init__(self, block_size):
        self._block_size = block_size

    def boost(self, solution, evaluator):

        block_size = self._block_size
        genotype_size = solution.get_genotype_size()
        genotype = solution.get_genotype()
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
        best_fitness = solution.get_fitness()
        for i, item in enumerate(blocks):
            perms = permutations(item)
            for k, perm in enumerate(perms):
                new_solution = []
                for j, block in enumerate(blocks):
                    if i == j:
                        new_solution += list(perm)
                    else:
                        new_solution += list(block)
                tmp_fitness = evaluator.evaluate(new_solution)
                if tmp_fitness > best_fitness:
                    best_fitness = tmp_fitness
                    solution.set_genotype(numpy.array(new_solution))
                    solution.set_fitness(tmp_fitness)
        return solution
