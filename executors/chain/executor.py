# -*- coding: utf-8 -*-

'''
Executor template.
'''

from helpers.setter import setter
from helpers.dict_wrapper import DictWrapper
from common.initializer import problem_init, algorithm_init


def execute(algorithms, problems, config):
    '''
    Execute all defined in config.
    '''
    common = setter(lambda: config.common, DictWrapper({}))
    algorithm_chain = setter(lambda: config.algorithms, [])

    for config in algorithm_chain:

        config.weak_merge(common)

        # evaluator configuration
        (problem_config, problem_operator) = problem_init(problems, config)

        # algorithm configuration
        (algorithm_config, algorithm) = algorithm_init(algorithms, config,
                                                       problem_config,
                                                       problem_operator)

        # execution
        solution = algorithm.engine.run(algorithm_config)
        print solution
