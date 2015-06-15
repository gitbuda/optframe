#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

import numpy as np
from helpers.path import unique_path
from helpers.grid_search import grid_item_container
from common.initializer import problem_init, algorithm_init

log = logging.getLogger(__name__)


def execute(algorithms, problems, config):
    '''
    '''
    # init
    grid = grid_item_container(config.grid)
    context = config.common

    # execution
    all_results = {}
    for element in grid:
        for it in range(int(config.repeat)):
            all_results.setdefault(element, [])
            context.hard_merge(element)

            # evaluator configuration
            (problem_config, problem_operator) = problem_init(problems,
                                                              context)

            # algorithm configuration
            (algorithm_config, algorithm) = algorithm_init(algorithms, context,
                                                           problem_config,
                                                           problem_operator)

            # algorithm execution
            solution = algorithm.engine.run(algorithm_config)

            all_results[element].append(solution)

    # calculate median values
    for key in all_results:
        all_results[key] = \
            np.median(map(lambda x: x.fitness.value, all_results[key]))

    # store best parameters
    params, median = min(all_results.items(), key=lambda x: x[1])
    output_max_path = unique_path('output', 'grid_search-%s-%s' %
                                  (context.algorithm, context.problem))
    params.store(output_max_path)
    print params, median

    # store heat map
    output_heatmap_path = unique_path('output', 'heatmap-%s-%s' %
                                      (context.algorithm, context.problem))
    with open(output_heatmap_path, 'w') as f:
        for params, median in all_results.items():
            for param in sorted(params.keys()):
                f.write('%s, ' % str(params[param]))
            f.write('%s\n' % str(median))
    print all_results
