# -*- coding: utf-8 -*-

'''
Pyramid Genetic Algorithm is variation of genetic algorithm
in which population size is unlimited. Solutions are stored
inside pyramid structure.

TODO: finis this.
'''

import logging
from common.limit import Limit
from common.solution_writer import write

log = logging.getLogger(__name__)


def run(context):
    '''
    Run PGA
    '''
    # setup
    evaluator = context.evaluate_operator
    cross_operator = context.cross_operator
    mutation_operator = context.mutation_operator
    init_solution_operator = context.init_solution_operator
    solution_operator = context.solution_operator
    selection_operator = context.selection_operator
    local_search = context.local_search
    best_store = context.best_store
    iteration_counter = context.iteration_counter

    with Limit(context.config):

        populations = list()
        populations.append(list())
        solutions = set()

        while True:

            # initial iteration solution
            if solution_operator is not None:
                solution = solution_operator.next()
            else:
                solution = init_solution_operator.generate(1)[0]
            solution.fitness = evaluator.evaluate(solution)
            solution = local_search.search(solution)

            solution_tuple = solution.create_tuple()
            if solution_tuple not in solutions:
                solutions.add(solution_tuple)
                populations[0].append(solution)
                best_store.try_store(solution)
            else:
                continue

            # pyramid iteration
            for pop_index in xrange(len(populations)):

                population = populations[pop_index]

                # select, cross, mutate and evaluate
                p_solution = selection_operator.select(population)[0]
                new_solution = cross_operator.cross(p_solution, solution)
                mutation_operator.mutate(new_solution)
                new_solution.fitness = evaluator.evaluate(new_solution)

                # add solution to a pyramid population
                solution_tuple = new_solution.create_tuple()
                if new_solution.fitness > p_solution.fitness:
                    if solution_tuple not in solutions:
                        solutions.add(solution_tuple)
                        next_index = pop_index + 1
                        if next_index == len(populations):
                            population = list()
                            populations.append(population)
                        populations[next_index].append(new_solution)
                        solution = new_solution
                        best_store.try_store(solution)

            iteration_counter.increase(best_store.best_solution)

    print "Best: %s" % best_store.best_solution.fitness.value
    write(best_store.best_solution, context.output_dir)

    return best_store.best_solution
