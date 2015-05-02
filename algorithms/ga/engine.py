#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from common.best_store import BestStore

log = logging.getLogger(__name__)


def evaluate_and_sort(population, evaluator):
    for solution in population:
        solution.fitness = evaluator.evaluate(solution)
    population.sort(key=lambda x: x.fitness, reverse=True)


def run(context):

    log.info("GA start")

    best_store = BestStore()
    best_store.configure(context.config)

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

    # initial population
    population = population_operator.generate()
    evaluate_and_sort(population, evaluator)
    best_store.try_store(population[0])

    try:

        for i in termination_operator(max_iterations):

            new_population = population[0:best_to_next_number]

            for j in range(population_size - best_to_next_number):

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

    except Exception as e:
        # import traceback
        # traceback.print_exc()
        log.info(e)

    return best_store.best_solution
