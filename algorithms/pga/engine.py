#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Pyramid Genetic Algorithm
'''

import logging

from common.best_store import BestStore
from common.solution import Solution
from common.selection.tournament import Tournament

log = logging.getLogger(__name__)


def run(context):

    evaluator = context.evaluate_operator
    box_operator = context.box_operator
    cross_operator = context.cross_operator
    mutation_operator = context.mutation_operator
    solution_number = context.solution_number
    tournament = Tournament()

    best_store = BestStore()
    best_store.configure(context.config)

    try:
        populations = [[]]
        solutions = set()

        while True:

            # initial iteration solution
            solution = Solution(box_operator.generate())
            solution.fitness = evaluator.evaluate(solution.box)
            solution_tuple = tuple(solution.box)
            if solution_tuple not in solutions:
                solutions.add(solution_tuple)
                populations[0].append(solution)
                best_store.try_store(solution.fitness, solution)

            # pyramid iteration
            for population_index in xrange(len(populations)):
                log.info("Population index: %s population len: %s" %
                         (population_index, len(populations)))
                population = populations[population_index]
                log.info("Fitness before PGA core: %s" % solution.fitness)
                pyramid_solution = tournament.select(population)
                new_solution = Solution()
                new_solution.box = cross_operator.cross(pyramid_solution.box,
                                                        solution.box)
                mutation_operator.mutate(new_solution.box)
                new_solution.fitness = evaluator.evaluate(new_solution.box)
                if new_solution.fitness >= solution.fitness:
                    solution_tuple = tuple(new_solution.box)
                    if solution_tuple not in solutions:
                        solutions.add(solution_tuple)
                        next_population_index = population_index + 1
                        if next_population_index == len(populations):
                            population = []
                            populations.append(population)
                        populations[next_population_index].append(new_solution)
                        solution = new_solution
                        log.info("Added to %d with fitness %f" %
                                 (next_population_index, solution.fitness))
                        best_store.try_store(solution.fitness, solution)
                    else:
                        break
                else:
                    break

            log.info("End of pyramid iteration\n")
            if len(solutions) >= solution_number:
                break
    except Exception as e:
        log.info(e)

    print best_store.best_solution.box, best_store.best_fitness

    return (best_store.best_solution, best_store.best_fitness)
