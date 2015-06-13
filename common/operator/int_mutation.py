# -*- coding: utf-8 -*-

'''
The operator iterates through ints and
with probabilty of mutataion_factor set the
selected bit on randomly chosen value from
domain.
'''

import random


class IntMutationOperator(object):

    def configure(self, config):
        '''
        Setup mutation factor and min, max int values
        '''
        self.mutation_factor = float(config.mutation_factor)
        self.min = int(config.solution_structure.int.min)
        self.max = int(config.solution_structure.int.max)
        return self

    def mutate(self, genes):
        '''
        '''
        # print "before ", genes
        for i, gene in enumerate(genes):
            random_float = random.random()
            if random_float < self.mutation_factor:
                genes[i] = random.randint(self.min, self.max)
        # print "after ", genes
