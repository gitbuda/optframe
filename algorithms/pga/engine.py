#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Pyramid Genetic Algorithm
'''

import random
import logging

from common.best_store import BestStore

log = logging.getLogger(__name__)


def run(context):

    evaluator = context.evaluate_operator
    box_operator = context.box_operator
    cross_operator = context.cross_operator
    mutation_operator = context.mutation_operator
    solution_number = context.solution_number

    best_store = BestStore()
    best_store.configure(context.config)

    try:
        populations = [[]]
        solutions = set()

        while True:

            # initial solution
            solution = box_operator.generate()
            fitness = evaluator.evaluate(solution)
            solution_tuple = tuple(solution)
            if solution_tuple not in solutions:
                solutions.add(solution_tuple)
                populations[0].append(solution)
                best_store.try_store(fitness, solution)

            # pyramid iteration
            for population_index in xrange(len(populations)):
                log.info("Population index: %s population len: %s" %
                         (population_index, len(populations)))
                population = populations[population_index]
                old_fitness = fitness
                log.info("Fitness before PGA core: %s" % old_fitness)
                better_index = random.randint(0, len(population) - 1)
                better = population[better_index]
                solution = cross_operator.cross(better, solution)
                mutation_operator.mutate(solution)
                new_fitness = evaluator.evaluate(solution)
                if new_fitness >= old_fitness:
                    solution_tuple = tuple(solution)
                    if solution_tuple not in solutions:
                        solutions.add(solution_tuple)
                        next_population_index = population_index + 1
                        if next_population_index == len(populations):
                            population = []
                            populations.append(population)
                        populations[next_population_index].append(solution)
                        log.info("Added to %d with fitness %f" %
                                 (next_population_index, new_fitness))
                        best_store.try_store(new_fitness, solution)
                else:
                    break

            log.info("End of pyramid iteration\n")
            if len(solutions) >= solution_number:
                break
    except Exception as e:
        log.info(e)

    return (best_store.best_solution, best_store.best_fitness)
