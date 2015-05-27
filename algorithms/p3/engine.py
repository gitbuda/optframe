#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
P3 algorithm.

Python implementation of:
https://github.com/brianwgoldman/Parameter-less_Population_Pyramid
'''

import uuid
import logging
from common.limit import Limit
from common.lt_population import LTPopulation

log = logging.getLogger(__name__)


def run(context):
    '''
    The algorithm execution method.
    '''
    log.info("P3 start")

    # operators and parameters
    evaluator = context.evaluate_operator
    best_store = context.best_store
    solution_operator = context.solution_operator
    iteration_counter = context.iteration_counter
    collection_operator = context.collection_operator
    solution_structure = context.solution_structure
    local_search = context.local_search
    cluster_cross = context.cluster_cross

    with Limit(context.config):

        solutions = set()
        populations = [LTPopulation(solution_structure)]

        while True:

            # take the initial solution from solution_operator
            # or from collection_operator, the solution operator is
            # problem specific, on the other hand collection operator
            # is generic and it will return a random solution,
            # collection operator returns a list of solutions
            # and the algorithm takes only one solution
            if solution_operator is not None:
                solution = solution_operator.next()
            else:
                solution = collection_operator.generate(1)[0]

            # evaluate the solution
            solution.fitness = evaluator.evaluate(solution)

            # apply local search
            solution = local_search.search(solution)

            # add solution into the population (into the
            # first level of the pyramid)
            solution_tuple = solution.create_tuple()
            if solution_tuple not in solutions:
                solutions.add(solution_tuple)
                populations[0].add(solution)
                best_store.try_store(solution)

            # one pyramid loop
            for population_index in xrange(len(populations)):
                population = populations[population_index]
                old_fitness = solution.fitness.deep_copy()
                cluster_cross.cross(solution, population.solutions,
                                    population.clusters)
                new_fitness = solution.fitness

                if new_fitness >= old_fitness:
                    solution_tuple = solution.create_tuple()
                    if solution_tuple not in solutions:
                        solutions.add(solution_tuple)
                        next_population_index = population_index + 1
                        if next_population_index == len(populations):
                            population = LTPopulation(solution_structure)
                            populations.append(population)
                        populations[next_population_index].add(solution)
                        best_store.try_store(solution)
                else:
                    break

            # stop the algorithm if solution number limit is
            # reached
            if len(solutions) >= context.solution_number:
                break

            # increase iteration counter
            iteration_counter.increase()

    # store the best solution
    best_fitness = best_store.best_solution.fitness.value
    output_path = '%s/f%s-%s.solution' % (context.output_dir,
                                          best_fitness, uuid.uuid4().hex)
    best_store.best_solution.persist(output_path)

    return best_store.best_solution
