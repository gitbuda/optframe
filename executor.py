#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
optframe executor (initial script)
'''

import logging

from helpers.loader import load_json, DictWrapper
from helpers.arguments import get_arg
from helpers.setter import setter
from helpers.load_package import load_package
from os.path import join as path_join
from statistics.writer import write

PROBLEMS_DIRNAME = 'problems'
ALGORITHMS_DIRNAME = 'algorithms'
CONFIG_FILE_NAME = 'config.json'
OUTPUT_DIR_NAME = 'output'


class ResultDTO(object):
    def __init__(self):
        self.fitness_container = []
        self.evaluations_container = []


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    log.info("Executor start")

    # load modules (algorithms and problems)
    problems = load_package(PROBLEMS_DIRNAME)
    algorithms = load_package(ALGORITHMS_DIRNAME)

    # load config
    config_file_name = get_arg('-c', CONFIG_FILE_NAME)
    execution_context = load_json(config_file_name)
    common = setter(lambda: execution_context.common, DictWrapper())

    results = {}
    for run in execution_context.runs:
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
            problem_config_path = path_join(PROBLEMS_DIRNAME,
                                            problem,
                                            CONFIG_FILE_NAME)
            problem_config = load_json(problem_config_path)
            output_path = path_join(PROBLEMS_DIRNAME,
                                    problem,
                                    OUTPUT_DIR_NAME)
            problem_config.hard_merge(run)
            problem_config.output_path = output_path
            evaluator.configure(problem_config)

            # algorithm configuration
            algorithm_modul = algorithms[algorithm]
            algorithm_config_path = path_join(ALGORITHMS_DIRNAME,
                                              algorithm,
                                              CONFIG_FILE_NAME)
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
            results.setdefault(identifier, ResultDTO())
            results[identifier].fitness_container.append(best_fitness)
            results[identifier].evaluations_container.append(
                evaluator.evaluation_counter.evaluations_number)

    write(results)

    log.info("Executor end")
