#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
P3 algorithm.
'''

import logging
import uuid

from common.lt_population import LTPopulation
from helpers.solution_writer import SolutionWriter

log = logging.getLogger(__name__)


def run(context):
    '''
    '''

    evaluator = context.evaluate_operator
    best_store = context.best_store
    solution_operator = context.solution_operator
    iteration_counter = context.iteration_counter
    collection_operator = context.collection_operator
    solution_structure = context.solution_structure
    local_search = context.local_search
    cluster_cross = context.cluster_cross
    writer = SolutionWriter()

    try:

        solutions = set()
        populations = [LTPopulation(solution_structure)]

        while True:

            # increase iteration counter
            iteration_counter.increase()

            if solution_operator is not None:
                solution = solution_operator.next()
            else:
                solution = collection_operator.generate(1)[0]

            solution.fitness = evaluator.evaluate(solution)

            solution = local_search.search(solution)

            solution_tuple = solution.create_tuple()
            if solution_tuple not in solutions:
                solutions.add(solution_tuple)
                populations[0].add(solution)
                best_store.try_store(solution)

            for population_index in xrange(len(populations)):
                log.info("Population index: %s population len: %s" %
                         (population_index, len(populations)))
                population = populations[population_index]
                old_fitness = solution.fitness.deep_copy()
                log.info("Fitness before p3 core: %s" % old_fitness.value)
                cluster_cross.cross(solution, population.solutions,
                                    population.clusters)
                new_fitness = solution.fitness

                if new_fitness >= old_fitness:
                    solution_tuple = solution.create_tuple()
                    print solution_tuple
                    if solution_tuple not in solutions:
                        solutions.add(solution_tuple)
                        next_population_index = population_index + 1
                        if next_population_index == len(populations):
                            population = LTPopulation(solution_structure)
                            populations.append(population)
                        populations[next_population_index].add(solution)
                        log.info("Added to %d with fitness %f" %
                                 (next_population_index, new_fitness.value))
                        best_store.try_store(solution)
                else:
                    break

            log.info("End of pyramid iteration\n")
            if len(solutions) >= context.solution_number:
                break

    except Exception as e:
        import traceback
        traceback.print_exc()
        log.info(e)

    best_fitness = best_store.best_solution.fitness.value
    log.info("Best fitness: " + str(best_fitness))
    output_path = '%s/f%s-%s.solution' % (context.output_dir,
                                          best_fitness, uuid.uuid4().hex)
    log.info("Output path: " + output_path)
    writer.write(output_path, best_store.best_solution)

    return best_store.best_solution
