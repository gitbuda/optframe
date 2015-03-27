#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import logging

log = logging.getLogger(__name__)

# config.evaluate_operator
# config.mutation_factor
# config.crossover_factor
# config.solution_number


def run(config):

    evaluator = config.evaluate_operator

    solution = [random.randint(0, 1) for i in xrange(256)]

    populations = [[0]]

    for i in xrange(10):
        for population_index in xrange(len(populations)):
            random_number = random.random()
            if random_number > 0.2:
                next_population_index = population_index + 1
                if next_population_index == len(populations):
                    populations.append([])
                    populations[next_population_index].append(next_population_index)
                else:
                    populations[population_index].append(population_index)
            else:
                break

    sizes = map(len, populations)
    print sizes

    best_genotype = solution
    best_fitness = evaluator.evaluate(solution)

    print best_fitness

    return (best_genotype, best_fitness)
