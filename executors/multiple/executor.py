#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

from common.execution_result import ExecutionResult
from common.initializer import problem_init, algorithm_init
from helpers.loader import DictWrapper
from helpers.setter import setter
from statistics.writer import write


def execute(algorithms, problems, config):
    '''
    '''
    # init
    common = setter(lambda: config.common, DictWrapper())
    results = {}

    # execution
    for run in config.runs:
        run.weak_merge(common)
        for problem_run in xrange(int(run.run_number)):

            # evaluator configuration
            (problem_config, problem_operator) = problem_init(problems, run)

            # algorithm configuration
            (algorithm_config, algorithm) = algorithm_init(algorithms, run,
                                                           problem_config,
                                                           problem_operator)

            # execution
            solution = algorithm.engine.run(algorithm_config)
            fitness = solution.fitness.value

            # results
            identifier = run.identifier
            evaluator = problem_operator.evaluator
            results.setdefault(identifier, ExecutionResult())
            results[identifier].fitness_container.append(fitness)
            results[identifier].evaluations_container.append(
                evaluator.evaluation_counter.evaluations_number)

    # write results
    write(results)
