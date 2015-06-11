# -*- coding: utf-8 -*-

'''
Executor template.
'''

from helpers.setter import setter
from helpers.dict_wrapper import DictWrapper


def execute(algorithms, problems, config):
    '''
    Execute all defined in config.
    '''
    common = setter(lambda: config.common, DictWrapper({}))
    algorithms = setter(lambda: config.algorithms, [])

    for config in algorithms:
        config.weak_merge(common)
        print config

        # # evaluator configuration
        # (problem_config, problem_operator) = problem_init(problems, run)

        # # algorithm configuration
        # (algorithm_config, algorithm) = algorithm_init(algorithms, run,
        #                                                problem_config,
        #                                                problem_operator)

        # # execution
        # solution = algorithm.engine.run(algorithm_config)
