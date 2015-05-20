#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from common.limit import Limit

log = logging.getLogger(__name__)


def evaluate_and_sort(population, evaluator):
    for solution in population:
        solution.fitness = evaluator.evaluate(solution)
    population.sort(key=lambda x: x.fitness, reverse=True)


def run(context):

    log.info("GA start")

    # operators and parameters
    termination_operator = context.termination_operator
    evaluator = context.evaluate_operator
    cross_operator = context.cross_operator
    mutation_operator = context.mutation_operator
    selection_operator = context.selection_operator
    population_operator = context.population_operator
    population_size = context.population_size
    max_iterations = context.max_iterations
    best_to_next_number = context.best_to_next_number
    iteration_counter = context.iteration_counter
    best_store = context.best_store

    # initial population
    population = population_operator.generate()
    evaluate_and_sort(population, evaluator)
    best_store.try_store(population[0])

    with Limit(context.config):

        while True:

            new_population = population[0:best_to_next_number]

            for j in xrange(population_size - best_to_next_number):

                # select pair
                selected_pair = selection_operator.select(population, 2)
                better = selected_pair[0]
                worse = selected_pair[1]

                # crossover and mutation
                new_solution = cross_operator.cross(better, worse)
                mutation_operator.mutate(new_solution)
                new_population.append(new_solution)

            population = new_population

            evaluate_and_sort(population, evaluator)
            best_store.try_store(population[0])

            iteration_counter.increase(best_store.best_solution)

    return best_store.best_solution
