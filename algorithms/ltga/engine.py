#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Linkage Tree Genetic Algorithm.
For now algorithm supports only bit and permutation
box.
'''

import random
import logging
from helpers.array_tools import swap
from helpers.array_tools import permutation_swap
from common.lt_population import LTPopulation
from common.constants import BIT_BOX_KEY, PERMUTATION_BOX_KEY

log = logging.getLogger(__name__)


def structure_swap(solution1, solution2, cluster, key):
    '''
    Swap elements in the solution boxes defined
    with key on the indices stored in the cluster.
    Returns deep copies of solutions.
    '''

    copy_1 = solution1.deep_copy()
    copy_2 = solution2.deep_copy()
    a = copy_1.container[key]
    b = copy_2.container[key]

    if key == BIT_BOX_KEY:
        swap(a, b, cluster)
    elif key == PERMUTATION_BOX_KEY:
        permutation_swap(a, b, cluster)

    return copy_1, copy_2


def run(context):
    '''
    LTGA executor run function.
    '''

    # paramaters and operators
    solution_structure = context.solution_structure
    evaluator = context.evaluate_operator
    best_store = context.best_store
    iteration_counter = context.iteration_counter
    collection_operator = context.collection_operator
    local_search = context.local_search

    try:
        # generate initial population
        population = LTPopulation(solution_structure)
        collection = collection_operator.generate()
        for solution in collection:
            solution.fitness = evaluator.evaluate(solution)
            solution = local_search.search(solution)
            population.add(solution, False)
        population_size = len(population.solutions)

        while True:
            # increase iteration counter
            iteration_counter.increase()

            # evaluate initial population
            for solution in population.solutions:
                solution.fitness = evaluator.evaluate(solution)
                best_store.try_store(solution)

            # build clusters
            population.recalculate_population()
            linkage_tree = population.clusters

            # LTGA core
            for key in solution_structure.keys():
                for cluster in linkage_tree[key]:
                    first, second = random.sample(range(population_size), 2)
                    a = population.solutions[first]
                    b = population.solutions[second]
                    # TODO: this kind of swap is bad for permutation
                    # box -> create different type of 'crossover'
                    off_a, off_b = structure_swap(a, b, cluster, key)
                    fit_a, fit_b = a.fitness, b.fitness
                    off_a.fitness = evaluator.evaluate(off_a)
                    off_b.fitness = evaluator.evaluate(off_b)
                    fit_off_a, fit_off_b = off_a.fitness, off_b.fitness
                    if fit_off_a >= fit_a and fit_off_a >= fit_b \
                            and fit_off_b >= fit_a and fit_off_b >= fit_b:
                        population.solutions[first] = off_a
                        population.solutions[second] = off_b
                        best_store.try_store(off_a)
                        best_store.try_store(off_b)

    except Exception as e:
        import traceback
        traceback.print_exc()
        log.info(e)

    return best_store.best_solution


if __name__ == '__main__':
    pass
