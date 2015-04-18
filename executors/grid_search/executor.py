#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

from common.best_store import BestStore
from common.initializer import problem_init, algorithm_init
from helpers.grid_search import grid_item_container
from helpers.path import unique_path

log = logging.getLogger(__name__)


def execute(algorithms, problems, config):
    '''
    '''
    # init
    grid = grid_item_container(config.grid)
    context = config.common
    best_store = BestStore()

    # execution
    for element in grid:
        context.hard_merge(element)

        # evaluator configuration
        (problem_config, problem_operator) = problem_init(problems, context)

        # algorithm configuration
        (algorithm_config, algorithm) = algorithm_init(algorithms, context,
                                                       problem_config,
                                                       problem_operator)

        (solution, fitness) = algorithm.engine.run(algorithm_config)

        best_store.try_store(fitness, solution, element)

    # prepare output
    context.hard_merge(best_store.best_config)
    output_path = unique_path('output', 'grid')

    # write output
    with open(output_path, 'w') as f:
        f.write(str(context))
        f.write('Fitness: %s\n' % str(best_store.best_fitness))
