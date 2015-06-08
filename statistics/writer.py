#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Write an execution results.
'''

import logging
import numpy as np

from helpers.path import unique_path
from helpers.dict_wrapper import DictWrapper

log = logging.getLogger(__name__)


def sorted_items(results):
    '''
    Sort items from the results dictionary and put
    them sorted in a list.

    Args:
        results: input dictionary
    '''
    items = results.items()
    items.sort(key=lambda x: str(x))
    return items


def write_fitness(results, prefix, identifier=''):
    '''
    Write fitness.
    '''
    file_name = unique_path('output', prefix)
    with open(file_name, 'w') as f:
        f.write("# fitness\n")
        f.write("# no min min_std mean max_std max id\n")
        i = 1
        for key, result in sorted_items(results):
            min_fit = np.min(result.fitness_container)
            max_fit = np.max(result.fitness_container)
            mean_fit = np.mean(result.fitness_container)
            std = np.std(result.fitness_container)
            min_std = mean_fit - std
            max_std = mean_fit + std
            result = '%s %3f %3f %3f %3f %3f %s\n' % \
                (str(i), min_fit, min_std, mean_fit, max_std, max_fit, key)
            f.write(result)
            i += 1


def write_eval(results, prefix, identifier=''):
    '''
    Write min, mean - std,  mean, mean + std, max
    '''
    file_name = unique_path('output', prefix)
    with open(file_name, 'w') as f:
        f.write("# evaluations\n")
        f.write("# no min min_std mean max_std max id\n")
        i = 1
        for key, result in sorted_items(results):
            min_eval = np.min(result.evaluations_container)
            max_eval = np.max(result.evaluations_container)
            mean_eval = np.mean(result.evaluations_container)
            std = np.std(result.evaluations_container)
            min_std = mean_eval - std
            max_std = mean_eval + std
            result = '%s %3f %3f %3f %3f %3f %s\n' % \
                (str(i), min_eval, min_std, mean_eval, max_std, max_eval, key)
            f.write(result)
            i += 1


def write_fitboxplot(results, prefix, identifier=''):
    '''
    Write boxplot data.
    '''
    file_name = unique_path('output', prefix)
    with open(file_name, 'w') as f:
        f.write('# fitness\n')
        f.write('# result algorithm\n')
        for key, result in results.items():
            for value in result.fitness_container:
                f.write('%s %s\n' % (key, str(value)))


def write_linelogy(container, prefix):
    '''
    Write line plot with logarighimic y-axis scale data.
    '''
    file_name = unique_path('output', prefix)
    output = DictWrapper({})
    output.hard_set('title', container.common_identifier)
    output.hard_set('xname', 'Problem size')
    output.hard_set('yname', 'Evaluations number')
    xvalues = sorted(list(container.problem_variants))
    yvalues = {}
    for identifier in container.order:
        result = container.results[identifier]
        algorithm = identifier.split('-')[0]
        yvalues.setdefault(algorithm, [])
        median = np.median(result.evaluations_container)
        yvalues[algorithm].append(median)
    output.hard_set('data', {'yvalues': yvalues, 'xvalues': xvalues})
    output.store(file_name)


def write(container):
    '''
    Write all
    '''
    write_fitness(container.results, 'fit', container.common_identifier)
    write_eval(container.results, 'eval', container.common_identifier)
    write_fitboxplot(container.results, 'fitness_boxplot',
                     container.common_identifier)
    write_linelogy(container, 'linelogy')


if __name__ == '__main__':
    pass
