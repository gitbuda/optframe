#!/usr/bin/env python
# -*- coding: utf-8 -*-

from helpers.config import read

from ga.selection import tournament
from ga.termination.termination import max_iteration
from ga.to_next.best_to_next_operator import BestToNextOperator
from ga.cross.bit_array import BitArrayCrossOperator
from ga.mutation.bit_mutation import BitMutationOperator
from ga.population.bit_array import BitArrayPopulationOperator

# gaconfig.ini keys
SECTION = 'GA'
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


class GAConfig(object):
    '''
        TODO: read all from conf file
    '''

    def __init__(self, path):

        # read config file
        self.settings = read(path)

        # prepare parameters
        mutation_factor = float(self.settings.get(SECTION, MUTATION_FACTOR))
        population_size = int(self.settings.get(SECTION, POPULATION_SIZE))
        population_operator = str(self.settings.get(SECTION, POPULATION_OPERATOR))
        iterations_number = int(self.settings.get(SECTION, ITERATIONS_NUMBER))
        crossover_factor = float(self.settings.get(SECTION, CROSSOVER_FACTOR))
        best_no = int(self.settings.get(SECTION, BEST_NO))
        genotype_size = int(self.settings.get(SECTION, GENOTYPE_SIZE))
        cross_mutation_factor = float(self.settings.get(SECTION,
                                                        CROSS_MUTATION_FACTOR))
        best_to_next_number = int(self.settings.get(SECTION,
                                                    BEST_TO_NEXT_NUMBER))

        population_operator = str(self.settings.get(SECTION, POPULATION_OPERATOR))
        mutation_operator = str(self.settings.get(SECTION, MUTATION_OPERATOR))
        cross_operator = str(self.settings.get(SECTION, CROSS_OPERATOR))

        # define all parameters
        self.parameters = {}
        self.parameters[MUTATION_FACTOR] = mutation_factor
        self.parameters[POPULATION_SIZE] = population_size
        self.parameters[CROSSOVER_FACTOR] = crossover_factor
        self.parameters[ITERATIONS_NUMBER] = iterations_number
        self.parameters[BEST_NO] = best_no
        self.parameters[GENOTYPE_SIZE] = genotype_size
        self.parameters[CROSS_MUTATION_FACTOR] = cross_mutation_factor
        self.parameters[BEST_TO_NEXT_NUMBER] = best_to_next_number
        self.parameters[POPULATION_OPERATOR] = population_operator

        # load all operators
        self.population_operators = {}
        self.population_operators['BitArrayPopulationOperator'] = \
            BitArrayPopulationOperator(population_size, genotype_size)

        self.cross_operators = {}
        self.cross_operators['BitArrayCrossOperator'] = \
            BitArrayCrossOperator()

        self.mutation_operators = {}
        self.mutation_operators['BitMutationOperator'] = \
            BitMutationOperator(mutation_factor)

        # choose all operators
        self.termination_operator = max_iteration
        self.population_operator = self.population_operators[population_operator]
        self.mutation_operator = self.mutation_operators[mutation_operator]
        self.cross_operator = self.cross_operators[cross_operator]
        self.selection_operator = tournament
        self.best_operator = BestToNextOperator(best_to_next_number)


if __name__ == '__main__':
    GAConfig()
