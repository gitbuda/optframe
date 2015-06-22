# -*- coding: utf-8 -*-

'''
Genetic Algorithm
'''

import logging
from common.limit import Limit
from helpers.setter import setter
from common.solution_writer import write

log = logging.getLogger(__name__)


def evaluate_and_sort(population, evaluator):
    '''
    Evaluate and sort whole population.

    Args:
        population: genetic algorithm population
        evaluator:  a problem evaluator
    '''
    # evaluate all solutions in the population
    for solution in population:
        solution.fitness = evaluator.evaluate(solution)

    # sort the population by fitness value because
    # the algorithm will take the best N solutions and
    # put them into the new population
    population.sort(key=lambda x: x.fitness, reverse=True)


def run(context):
    '''
    The algorithm execution function.
    '''
    log.info("GA start")

    # operators and parameters
    identifier = setter(lambda: context.config.identifier, None)
    evaluator = context.evaluate_operator
    cross_operator = context.cross_operator
    mutation_operator = context.mutation_operator
    selection_operator = context.selection_operator
    population_operator = context.population_operator
    solution_operator = context.solution_operator
    population_size = context.population_size
    best_to_next_number = context.best_to_next_number
    iteration_counter = context.iteration_counter
    best_store = context.best_store
    best_store.evaluator = evaluator

    # the algorithm has execution limits, when any of
    # these limit is reached the Limit object will
    # stop execution of the algorithm
    with Limit(context.config):

        # initial population
        if solution_operator:
            population = [solution_operator.next()
                          for x in range(population_size)]
        else:
            population = population_operator.generate()
        evaluate_and_sort(population, evaluator)
        best_store.try_store(population[0])

        while True:

            # take the best N solutions and put them into the
            # new population
            new_population = population[0:best_to_next_number]

            for j in xrange(population_size - best_to_next_number):

                # select pair
                selected_pair = selection_operator.select(population, 2)
                better = selected_pair[0]
                worse = selected_pair[1]

                # if solution_operator is not None:
                #     worse = solution_operator.next()
                # else:
                #     worse = selected_pair[1]

                # crossover and mutation
                new_solution = cross_operator.cross(better, worse)
                mutation_operator.mutate(new_solution)
                new_population.append(new_solution)

            population = new_population
            evaluate_and_sort(population, evaluator)

            # if the best solution from the population
            # is better then the one that is already stored
            # store the new best solution
            best_store.try_store(population[0])

            iteration_counter.increase(best_store.best_solution)

    log.info("GA end")

    write(best_store.best(evaluator), context.output_dir, identifier)

    return best_store.best(evaluator)
