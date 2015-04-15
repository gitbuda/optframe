#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import common.constants as CONF

from common.execution_result import ExecutionResult
from helpers.loader import load_json, DictWrapper
from helpers.setter import setter
from os.path import join as path_join
from statistics.writer import write


def execute(algorithms, problems, config):
    '''
    '''
    results = {}
    common = setter(lambda: config.common, DictWrapper())
    for run in config.runs:
        run.weak_merge(common)
        for problem_run in xrange(int(run.run_number)):
            problem = run.problem
            algorithm = run.algorithm

            try:
                solution_operator = \
                    problems[problem].solution_operator.SolutionOperator()
            except Exception:
                solution_operator = None

            # evaluator configuration
            evaluator = problems[problem].evaluator.Evaluator()
            problem_config_path = path_join(CONF.PROBLEMS_DIRNAME,
                                            problem,
                                            CONF.CONFIG_FILE_NAME)
            problem_config = load_json(problem_config_path)
            output_path = path_join(CONF.PROBLEMS_DIRNAME,
                                    problem,
                                    CONF.OUTPUT_DIR_NAME)
            problem_config.hard_merge(run)
            problem_config.output_path = output_path
            evaluator.configure(problem_config)

            # algorithm configuration
            algorithm_modul = algorithms[algorithm]
            algorithm_config_path = path_join(CONF.ALGORITHMS_DIRNAME,
                                              algorithm,
                                              CONF.CONFIG_FILE_NAME)
            algorithm_config = algorithm_modul.config.Config()
            algorithm_config.evaluate_operator = evaluator
            algorithm_config.solution_operator = solution_operator
            algorithm_config.load_problem_conf(problem_config)
            alg_conf = load_json(algorithm_config_path)
            algorithm_config.load_algorithm_conf(alg_conf)
            algorithm_config.problem = problem_config

            # execution
            (best, best_fitness) = \
                algorithm_modul.engine.run(algorithm_config)

            # results
            identifier = run.identifier
            results.setdefault(identifier, ExecutionResult())
            results[identifier].fitness_container.append(best_fitness)
            results[identifier].evaluations_container.append(
                evaluator.evaluation_counter.evaluations_number)
            write(results)
