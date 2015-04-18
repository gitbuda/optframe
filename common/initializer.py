#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging
import common.constants as CONF

from os.path import join as path_join
from helpers.loader import load_json
from helpers.setter import setter

log = logging.getLogger(__name__)


class ProblemOperator(object):
    '''
    '''

    def __init__(self):
        '''
        '''
        self.evaluator = None
        self.solution = None


def problem_init(problems, config):
    '''
    '''
    problem = config.problem

    solution_operator = setter(
        lambda: problems[problem].solution_operator.SolutionOperator(), None)

    evaluator = problems[problem].evaluator.Evaluator()
    problem_config_path = path_join(CONF.PROBLEMS_DIRNAME, problem,
                                    CONF.CONFIG_FILE_NAME)
    problem_config = load_json(problem_config_path)
    output_path = path_join(CONF.PROBLEMS_DIRNAME, problem,
                            CONF.OUTPUT_DIR_NAME)
    problem_config.hard_merge(config)
    problem_config.output_path = output_path
    evaluator.configure(problem_config)

    problem_operator = ProblemOperator()
    problem_operator.solution = solution_operator
    problem_operator.evaluator = evaluator

    return (problem_config, problem_operator)


def algorithm_init(algorithms, config, problem_config, problem_operator):
    '''
    '''
    algorithm = config.algorithm

    algorithm_modul = algorithms[algorithm]
    algorithm_config_path = path_join(CONF.ALGORITHMS_DIRNAME, algorithm,
                                      CONF.CONFIG_FILE_NAME)
    algorithm_config = algorithm_modul.config.Config()
    algorithm_config.evaluate_operator = problem_operator.evaluator
    algorithm_config.solution_operator = problem_operator.solution
    algorithm_config.load_problem_conf(problem_config)
    alg_conf = load_json(algorithm_config_path)
    algorithm_config.load_algorithm_conf(alg_conf)
    algorithm_config.problem = problem_config

    return (algorithm_config, algorithm_modul)


if __name__ == '__main__':
    pass
