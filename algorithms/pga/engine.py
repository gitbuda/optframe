#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Pyramid Genetic Algorithm
'''

import logging

from common.best_store import BestStore

log = logging.getLogger(__name__)


def run(context):

    evaluator = context.evaluate_operator
    cross_operator = context.cross_operator
    mutation_operator = context.mutation_operator
    solution_number = context.solution_number
    init_solution_operator = context.init_solution_operator
    selection_operator = context.selection_operator

    best_store = BestStore()
    best_store.configure(context.config)

    try:
        populations = [[]]
        solutions = set()

        while True:

            # initial iteration solution
            solution = init_solution_operator.generate(1)[0]
            solution.fitness = evaluator.evaluate(solution)
            solution_tuple = solution.create_tuple()
            if solution_tuple not in solutions:
                solutions.add(solution_tuple)
                populations[0].append(solution)
                best_store.try_store(solution)

            # pyramid iteration
            for population_index in xrange(len(populations)):
                log.info("Population index: %s population len: %s" %
                         (population_index, len(populations)))
                population = populations[population_index]
                log.info("Fitness before PGA core: %s" %
                         solution.fitness.value)
                pyramid_solution = selection_operator.select(population)[0]
                new_solution = cross_operator.cross(pyramid_solution,
                                                    solution)
                mutation_operator.mutate(new_solution)
                new_solution.fitness = evaluator.evaluate(new_solution)
                if new_solution.fitness >= solution.fitness:
                    solution_tuple = new_solution.create_tuple()
                    if solution_tuple not in solutions:
                        solutions.add(solution_tuple)
                        next_population_index = population_index + 1
                        if next_population_index == len(populations):
                            population = []
                            populations.append(population)
                        populations[next_population_index].append(new_solution)
                        solution = new_solution
                        log.info("Added to %d with fitness %f" %
                                 (next_population_index,
                                  solution.fitness.value))
                        best_store.try_store(solution)
                    else:
                        break
                else:
                    break

            log.info("End of pyramid iteration\n")
            if len(solutions) >= solution_number:
                break
    except Exception as e:
        log.info(e)

    print "Best: %s" % best_store.best_solution.fitness.value

    return best_store.best_solution
