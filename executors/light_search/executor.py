#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

from helpers.path import unique_path
from common.initializer import problem_init, algorithm_init
from helpers.loader import DictWrapper
from common.fitness import Fitness

log = logging.getLogger(__name__)


def execute(algorithms, problems, config):
    '''
    '''
    best_parameters = {}
    context = config.common

    # execution
    for param_name in config.grid.keys():
        best = None
        best_param = None
        for param in config.grid[param_name]:
            conf_instance = {}
            conf_instance[param_name] = param
            for other_param in config.grid.keys():
                if other_param == param_name:
                    continue
                elif other_param in best_parameters:
                    conf_instance[other_param] = best_parameters[other_param]
                else:
                    param_index = len(config.grid[other_param]) / 2
                    conf_instance[other_param] = \
                        config.grid[other_param][param_index]
            dict_wrap = DictWrapper(conf_instance)
            context.hard_merge(dict_wrap)
            tmp_best = []
            size = int(config.repeat)
            for iteration in xrange(size):
                best_parameters[param_name] = param

                # evaluator configuration
                (problem_config, problem_operator) = problem_init(problems,
                                                                  context)

                # algorithm configuration
                (algorithm_config, algorithm) = \
                    algorithm_init(algorithms, context, problem_config,
                                   problem_operator)

                # algorithm execution
                solution = algorithm.engine.run(algorithm_config)
                tmp_best.append(solution.fitness)
            mean = 1.0 * sum(map(lambda x: x.value, tmp_best)) / size
            print "-------------------"
            print mean
            print conf_instance
            print "-------------------"
            fitness = Fitness(mean, tmp_best[0].category)
            if best is None or best < fitness:
                best = fitness
                best_param = param
        best_parameters[param_name] = best_param

    print best_parameters

    # prepare output
    output_path = unique_path('output', 'search-%s-%s' %
                              (config.algorithm, config.problem))

    # write output
    with open(output_path, 'w') as f:
        f.write(str(best_parameters))
