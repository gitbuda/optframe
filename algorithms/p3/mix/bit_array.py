# -*- coding: utf-8 -*-

'''
Bit array mix operator.
'''

import random


class BitArrayMix(object):

    def __init__(self):
        pass

    def mix(self, solution, population, evaluator):
        '''
        Mix bit array solution with the population.
        '''

        clusters = population.get_clusters()
        solutions = population.solutions
        solutions_no = len(solutions)
        # donors = [i for i in xrange(solutions_no)]

        for cluster in clusters:
            # for index in donors:
            index = random.randint(0, solutions_no - 1)
            existing_solution = solutions[index]
            solution, different = self.donate(solution,
                                              existing_solution,
                                              cluster,
                                              evaluator)

        return solution

    def donate(self, solution, donor, cluster, evaluator):

        changed = False
        for gene in cluster:
            src_dnk = donor.get_genotype()
            dst_dnk = solution.get_genotype()

            dst_dnk[gene], src_dnk[gene] = src_dnk[gene], dst_dnk[gene]
            if src_dnk[gene] != dst_dnk[gene]:
                changed = True

        if changed:
            new_fitness = evaluator.evaluate(dst_dnk)
            old_fitness = solution.get_fitness()
            if new_fitness >= old_fitness:
                solution.set_fitness(new_fitness)
                for gene in cluster:
                    src_dnk[gene] = dst_dnk[gene]
            else:
                for gene in cluster:
                    dst_dnk[gene], src_dnk[gene] = \
                        src_dnk[gene], dst_dnk[gene]

        return (solution, changed)
