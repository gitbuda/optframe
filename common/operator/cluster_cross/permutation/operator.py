#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import random
import logging
from common.selection.tournament import Selection

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
        self.selection = Selection()

    def cross(self, box, solution, donors, clusters):
        '''
        Mix permutation solution with the population.
        '''
        genotype_len = len(solution.container[box])

        for cluster in clusters:
            index = random.randint(0, len(donors) - 1)
            existing_solution = donors[index]
            # existing_solution = self.selection.select(donors)[0]
            input_solution_copy = solution.deep_copy()

            used_genes = set()
            used_indices = set()
            solution_dnk = solution.container[box]
            src_dnk = existing_solution.container[box]
            dst_dnk = input_solution_copy.container[box]

            for gene in cluster:
                dst_dnk[gene] = src_dnk[gene]
                used_genes.add(src_dnk[gene])
                used_indices.add(gene)

            dst_index = 0
            for i in range(genotype_len):
                if solution_dnk[i] in used_genes:
                    continue
                while dst_index in used_indices:
                    dst_index += 1
                if dst_index == genotype_len:
                    break
                dst_dnk[dst_index] = solution_dnk[i]
                dst_index += 1
                used_genes.add(solution_dnk[i])

            old_fitness = solution.fitness
            new_fitness = self.evaluator.evaluate(input_solution_copy)

            if new_fitness >= old_fitness:
                solution.container[box] = dst_dnk
                solution.fitness = new_fitness

        return solution

if __name__ == '__main__':
    pass
