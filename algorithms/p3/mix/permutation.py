# -*- coding: utf-8 -*-

'''
Permutation mix operator.
'''

import random


class PermutationMix(object):

    def __init__(self):
        pass

    def mix(self, solution, population, evaluator):
        '''
        Mix permutation solution with the population.
        '''

        clusters = population.get_clusters()
        solutions = population.solutions
        solutions_no = len(solutions)
        genotype_len = len(solution.get_genotype())

        for cluster in clusters:
            index = random.randint(0, solutions_no - 1)
            existing_solution = solutions[index]
            input_solution_copy = solution.deep_copy()

            used_genes = set()
            solution_dnk = solution.get_genotype()
            src_dnk = existing_solution.get_genotype()
            dst_dnk = input_solution_copy.get_genotype()

            for gene in cluster:
                dst_dnk[gene] = src_dnk[gene]
                used_genes.add(src_dnk[gene])

            for i in range(genotype_len):
                if solution_dnk[i] in used_genes:
                    continue
                dst_dnk[i] = solution_dnk[i]
                used_genes.add(solution_dnk[i])

            new_fitness = evaluator.evaluate(dst_dnk)
            old_fitness = solution.get_fitness()

            if new_fitness >= old_fitness:
                solution.set_genotype(dst_dnk)
                solution.set_fitness(new_fitness)

        return solution
