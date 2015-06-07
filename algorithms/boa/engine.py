# -*- coding: utf-8 -*-

'''
Bayesian Optimization Algorithm
'''

import logging

from common.best_store import BestStore
from common.solution import Solution
from common.bayes.network import random_bitstr
from common.bayes.network import construct_network
from common.bayes.network import sample_from_network
from common.constants import BIT_BOX_KEY

log = logging.getLogger(__name__)


def run(context):
    '''
    BOA main function.
    '''
    # load parameters
    evaluator = context.evaluate_operator
    solution_size = context.solution_size
    iterations_number = context.iterations_number
    population_size = context.population_size
    select_size = context.select_size
    childern_number = context.childern_number
    max_edges = 3 * population_size

    best_store = BestStore()
    best_store.configure(context.config)

    try:

        population = []
        for x in xrange(population_size):
            box = random_bitstr(solution_size)
            solution = Solution({BIT_BOX_KEY: box})
            solution.fitness = evaluator.evaluate(solution)
            population.append(solution)

        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        for iteration in xrange(iterations_number):
            selected = population[:select_size]
            network = construct_network(selected, solution_size, max_edges)
            childrens = sample_from_network(selected, network, childern_number)
            for children in childrens:
                children.fitness = evaluator.evaluate(children)
            population = population[0:(population_size - select_size)] \
                + childrens
            population_size = len(population)
            max_edges = 3 * population_size
            population.sort(key=lambda x: x.fitness, reverse=True)
            first = population[0]
            best_store.try_store(first)

    except Exception as e:
        # import traceback
        # traceback.print_exc()
        log.info(e)

    return best_store.best_solution
