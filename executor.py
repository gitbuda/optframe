#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
optframe executor (initial script)
'''

import imp
import logging

from os import walk
from helpers.loader import load_json
from statistics.writer import write

PROBLEMS_DIRNAME = 'problems'
ALGORITHMS_DIRNAME = 'algorithms'

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    log.info("Executor start")

    # load all available problems
    (_, problem_names, _) = walk(PROBLEMS_DIRNAME).next()
    problems = {}
    for problem_name in problem_names:
        f, filename, desc = imp.find_module(problem_name, [PROBLEMS_DIRNAME])
        modul = imp.load_module(problem_name, f, filename, desc)
        problems[problem_name] = modul

    # load all available algorithms
    (_, algorithm_names, _) = walk(ALGORITHMS_DIRNAME).next()
    algorithms = {}
    for algorithm_name in algorithm_names:
        f, filename, desc = imp.find_module(algorithm_name,
                                            [ALGORITHMS_DIRNAME])
        modul = imp.load_module(algorithm_name, f, filename, desc)
        algorithms[algorithm_name] = modul

    results = {}

    execution_context = load_json('config.json')
    for iteration in xrange(int(execution_context.runs)):
        for problem in execution_context.problems:
            for algorithm in execution_context.algorithms:
                evaluator = problems[problem].evaluator.Evaluator()
                prob_conf_path = '%s/%s/config.json' % (PROBLEMS_DIRNAME,
                                                        problem)
                problem_config = load_json(prob_conf_path)
                output_path = '%s/%s/output' % (PROBLEMS_DIRNAME, problem)
                problem_config.output_path = output_path
                evaluator.configure(problem_config)
                algorithm_modul = algorithms[algorithm]
                alg_conf = '%s/%s/config.ini' % (ALGORITHMS_DIRNAME, algorithm)
                algorithm_config = algorithm_modul.config.Config()
                algorithm_config.evaluate_operator = evaluator
                algorithm_config.load_problem_conf(problem_config)
                algorithm_config.load_algorithm_conf(alg_conf)
                (best, best_fitness) = \
                    algorithm_modul.engine.run(algorithm_config)
                identifier = '%s, %s' % (problem, algorithm)
                results.setdefault(identifier, []).append(best_fitness)

    write(results)

    log.info("Executor end")
