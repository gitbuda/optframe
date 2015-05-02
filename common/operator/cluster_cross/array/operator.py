#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import random
import logging

log = logging.getLogger(__name__)


class Operator(object):
    '''
    '''

    def __init__(self):
        '''
        '''
        pass

    def configure(self, evaluator):
        '''
        '''

        self.evaluator = evaluator

    def cross(self, box_key, solution, donors, clusters):
        '''
        '''

        # donors_ind = [i for i in xrange(solutions_no)]
        donors_no = len(donors)

        for cluster in clusters:
            # for index in donors_ind:
            index = random.randint(0, donors_no - 1)
            existing_solution = donors[index]
            solution, different = self.donate(box_key,
                                              solution,
                                              existing_solution,
                                              cluster)

        return solution

    def donate(self, box_key, solution, donor, cluster):
        '''
        '''

        changed = False

        for gene in cluster:
            src_dnk = donor.container[box_key]
            dst_dnk = solution.container[box_key]

            dst_dnk[gene], src_dnk[gene] = src_dnk[gene], dst_dnk[gene]
            if src_dnk[gene] != dst_dnk[gene]:
                changed = True

        if changed:
            new_fitness = self.evaluator.evaluate(solution)
            old_fitness = solution.fitness
            if new_fitness >= old_fitness:
                solution.fitness = new_fitness
                for gene in cluster:
                    src_dnk[gene] = dst_dnk[gene]
            else:
                for gene in cluster:
                    dst_dnk[gene], src_dnk[gene] = \
                        src_dnk[gene], dst_dnk[gene]

        return (solution, changed)

if __name__ == '__main__':
    pass
