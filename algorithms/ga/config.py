#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algorithms.ga.selection import tournament
from algorithms.ga.termination.termination import max_iteration
from algorithms.ga.to_next.best_to_next_operator import BestToNextOperator
from algorithms.ga.population.bit_array import BitArrayPopulationOperator
from algorithms.ga.population.permutation import PermutationPopulationOperator

from common.operator.bit_cross import BitCrossOperator
from common.operator.bit_mutation import BitMutationOperator
from common.operator.permutation_cross import PermutationCrossOperator
from common.operator.permutation_mutation import PermutationMutationOperator

MUTATION_FACTOR = 'MutationFactor'
POPULATION_SIZE = 'PopulationSize'
CROSSOVER_FACTOR = 'CrossoverFactor'
CROSS_MUTATION_FACTOR = 'CrossMutationFactor'
ITERATIONS_NUMBER = 'IterationsNumber'
BEST_NO = 'BestNo'
GENOTYPE_SIZE = 'GenotypeSize'
BEST_TO_NEXT_NUMBER = 'BestToNextNumber'

MUTATION_OPERATOR = 'MutationOperator'
POPULATION_OPERATOR = 'PopulationOperator'
CROSS_OPERATOR = 'CrossOperator'


class Config(object):
    '''
        TODO: read all from conf file
    '''
    def __init__(self):
        self.parameters = {}

    def load_problem_conf(self, problem_config):
        self.config = problem_config

        if 'solution_type' in self.config:
            self.config.weak_set('cross_operator',
                                 '%sCrossOperator' %
                                 self.config.solution_type)
            self.config.weak_set('mutation_operator',
                                 '%sMutationOperator' %
                                 self.config.solution_type)
            self.config.weak_set('population_operator',
                                 '%sPopulationOperator' %
                                 self.config.solution_type)

    def load_algorithm_conf(self, algorithm_config):

        self.config.weak_merge(algorithm_config)

        # define all parameters
        self.parameters[MUTATION_FACTOR] = float(self.config.mutation_factor)
        self.parameters[POPULATION_SIZE] = int(self.config.population_size)
        self.parameters[CROSSOVER_FACTOR] = float(self.config.cross_factor)
        self.parameters[ITERATIONS_NUMBER] = int(self.config.iterations_number)
        self.parameters[BEST_NO] = int(self.config.best_no)
        self.parameters[CROSS_MUTATION_FACTOR] = \
            float(self.config.cross_mutation_factor)
        self.parameters[BEST_TO_NEXT_NUMBER] = \
            int(self.config.best_to_next_number)

        # load all operators
        self.population_operators = {}
        self.population_operators['bitPopulationOperator'] = \
            BitArrayPopulationOperator(self.parameters[POPULATION_SIZE],
                                       int(self.config.solution_size))
        self.population_operators['permutationPopulationOperator'] = \
            PermutationPopulationOperator(self.parameters[POPULATION_SIZE],
                                          int(self.config.solution_size))

        self.cross_operators = {}
        self.cross_operators['bitCrossOperator'] = \
            BitCrossOperator(self.parameters[CROSSOVER_FACTOR])
        self.cross_operators['permutationCrossOperator'] = \
            PermutationCrossOperator()

        self.mutation_operators = {}
        self.mutation_operators['bitMutationOperator'] = \
            BitMutationOperator(self.parameters[MUTATION_FACTOR])
        self.mutation_operators['permutationMutationOperator'] = \
            PermutationMutationOperator(self.parameters[MUTATION_FACTOR])

        # choose all operators
        self.termination_operator = max_iteration
        self.population_operator = \
            self.population_operators[self.config.population_operator]
        self.mutation_operator = \
            self.mutation_operators[self.config.mutation_operator]
        self.cross_operator = \
            self.cross_operators[self.config.cross_operator]
        self.selection_operator = tournament
        self.best_operator = \
            BestToNextOperator(self.parameters[BEST_TO_NEXT_NUMBER])


if __name__ == '__main__':
    pass
