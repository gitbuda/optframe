#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

from common.execution_result import ExecutionResult
from common.execution_container import ExecutionContainter
from common.initializer import problem_init, algorithm_init
from helpers.loader import DictWrapper
from helpers.setter import setter
from statistics.writer import write


def execute(algorithms, problems, config):
    '''
    '''
    # init
    common = setter(lambda: config.common, DictWrapper())
    container = ExecutionContainter()
    container.common_identifier = setter(
        lambda: common.common_identifier, None)

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
            solution_size = setter(
                lambda: algorithm_config.config.solution_size, 0)
            identifier = run.identifier
            evaluator = problem_operator.evaluator
            container.results.setdefault(identifier, ExecutionResult())
            container.results[identifier].fitness_container.append(fitness)
            container.results[identifier].evaluations_container.append(
                evaluator.evaluation_counter.evaluations_number)
            container.problem_variants.add(solution_size)

    # write results
    write(container)
