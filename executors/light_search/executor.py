#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging
import numpy as np
from helpers.path import unique_path
from common.initializer import problem_init, algorithm_init
from helpers.dict_wrapper import DictWrapper
from common.fitness import Fitness
from helpers.setter import setter

log = logging.getLogger(__name__)


def execute(algorithms, problems, config):
    '''
    '''
    best_parameters = {}
    context = config.common

    # execution
    heatmap = []
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
            median = np.median(map(lambda x: x.value, tmp_best))
            print "-------------------"
            print map(lambda x: x.value, tmp_best)
            print median
            print conf_instance
            print "-------------------"
            heatmap.append((conf_instance, median))
            fitness = Fitness(median, tmp_best[0].category)
            if best is None or best < fitness:
                best = fitness
                best_param = param
        best_parameters[param_name] = best_param

    print best_parameters

    # write heatmap
    identifier = setter(lambda: context.identifier, context.problem)
    output_path = unique_path('output', 'heatmap-%s-%s' %
                              (context.algorithm, identifier))
    with open(output_path, 'w') as f:
        # TODO: add header
        for config, median in heatmap:
            for param in sorted(config.keys()):
                f.write('%s, ' % str(config[param]))
            f.write('%s\n' % str(median))

    print 'heatmap', heatmap

    # prepare output
    output_path = unique_path('output', 'search-%s-%s' %
                              (context.algorithm, identifier))

    # write output
    DictWrapper(best_parameters).store(output_path)
