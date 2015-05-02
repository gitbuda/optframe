#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging
import random
from common.constants import PERMUTATION_BOX_KEY

log = logging.getLogger(__name__)


class Operator(object):

    def __init__(self):
        '''
        '''
        pass

    def configure(self, evaluator):
        '''
        '''
        self.evaluator = evaluator

    def cross(self, solution, donors, clusters):
        '''
        Mix permutation solution with the population.
        '''

        solutions = donors
        solutions_no = len(solutions)
        genotype_len = len(solution.container[PERMUTATION_BOX_KEY])

        for cluster in clusters:
            index = random.randint(0, solutions_no - 1)
            existing_solution = solutions[index]
            input_solution_copy = solution.deep_copy()

            used_genes = set()
            solution_dnk = solution.container[PERMUTATION_BOX_KEY]
            src_dnk = existing_solution.container[PERMUTATION_BOX_KEY]
            dst_dnk = input_solution_copy.container[PERMUTATION_BOX_KEY]

            for gene in cluster:
                dst_dnk[gene] = src_dnk[gene]
                used_genes.add(src_dnk[gene])

            for i in range(genotype_len):
                if solution_dnk[i] in used_genes:
                    continue
                dst_dnk[i] = solution_dnk[i]
                used_genes.add(solution_dnk[i])

            new_fitness = self.evaluator.evaluate(input_solution_copy)
            old_fitness = solution.fitness

            if new_fitness >= old_fitness:
                solution.container[PERMUTATION_BOX_KEY] = dst_dnk
                solution.fitness = new_fitness

        return solution

if __name__ == '__main__':
    pass
