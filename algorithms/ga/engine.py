#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from algorithms.ga.optimization.structure.population import Population
from algorithms.ga.optimization.structure.genotype import Genotype
from algorithms.ga.config import BEST_TO_NEXT_NUMBER
# from algorithms.ga.config import CROSS_MUTATION_FACTOR
from common.best_store import BestStore
from common.evaluator_exception import EvaluatorException

log = logging.getLogger(__name__)


def evaluate(population, best, best_fitness, evaluate_operator, best_operator):

    # evaluate all genotypes
    # evaluations is array of touples [(index, fitness)]
    evaluations = []
    for j, genotype in enumerate(population.genotypes):
        fitness = evaluate_operator.evaluate(genotype.genes)
        evaluations.append((j, fitness))

    best_array = best_operator.to_next(evaluations)
    if best_array[0][1] > best_fitness:
        best = population.genotypes[best_array[0][0]]
        best_fitness = best_array[0][1]

    return (evaluations, best_array, best, best_fitness)


def run(conf):

    log.info("GA start")
    log.info("parameters\n%s" % conf.config)

    best_store = BestStore()

    # operators
    termination_operator = conf.termination_operator
    evaluate_operator = conf.evaluate_operator
    cross_operator = conf.cross_operator
    mutation_operator = conf.mutation_operator
    selection_operator = conf.selection_operator
    population_operator = conf.population_operator
    best_operator = conf.best_operator

    # parameters
    population_size = conf.parameters['PopulationSize']
    max_iterations = conf.parameters['IterationsNumber']
    best_to_next_number = conf.parameters[BEST_TO_NEXT_NUMBER]
    # cross_mutation_factor = conf.parameters[CROSS_MUTATION_FACTOR]

    population = population_operator.generate()
    best = population.genotypes[0]
    best_fitness = evaluate_operator.evaluate(population.genotypes[0].genes)

    try:
        # evaluation process
        for i in termination_operator(max_iterations):

            (evaluations, best_array, best, best_fitness) = \
                evaluate(population, best, best_fitness, evaluate_operator,
                         best_operator)
            best_store.try_store(best_fitness, best)

            new_population = Population()
            for k, item in enumerate(best_array):
                new_population.append(population.genotypes[item[0]])

            for j in range(population_size - best_to_next_number):

                # select pair
                selected_pair = selection_operator.select(evaluations)
                better_genes = population.genotypes[selected_pair[0][0]].genes
                worse_genes = population.genotypes[selected_pair[1][0]].genes

                # partial
                # if random.random() < cross_mutation_factor:
                #    new_genes = cross_operator.cross(better_genes,
                #                                     worse_genes)
                #    new_genotype = Genotype(new_genes)
                #    new_population.append(new_genotype)
                # else:
                #     new_genotype = Genotype(better_genes)
                #     mutation_operator.mutate(new_genotype.genes)
                #     new_population.append(new_genotype)

                # all
                new_genes = cross_operator.cross(better_genes, worse_genes)
                new_genotype = Genotype(new_genes)
                mutation_operator.mutate(new_genotype.genes)
                new_population.append(new_genotype)

            population = new_population

            (evaluations, best_array, best, best_fitness) = \
                evaluate(population, best, best_fitness, evaluate_operator,
                         best_operator)
            best_store.try_store(best_fitness, best)

            log.info('iteration = %s; cost = %s; genotype = %s' %
                     (i, best_fitness, best.genes))

    except EvaluatorException:
        pass

    return (best, best_fitness)
