#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import uuid
import logging
import datetime
import numpy as np

log = logging.getLogger(__name__)


def unique_file_name(prefix):
    file_name = 'output/%s-%s-%s' % \
        (prefix,
         uuid.uuid4().hex,
         datetime.datetime.utcnow().strftime('%d-%m-%Y-%H-%M'))
    return file_name


def sorted_items(results):
    items = results.items()
    items.sort(key=lambda x: str(x))
    return items


def write_fitness(results, prefix):
    file_name = unique_file_name(prefix)
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
            result = '%s %s %s %s %s %s %s\n' % \
                (str(i), min_fit, min_std, mean_fit, max_std, max_fit, key)
            f.write(result)
            i += 1


def write_eval(results, prefix):
    file_name = unique_file_name(prefix)
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
            result = '%s %s %s %s %s %s %s\n' % \
                (str(i), min_eval, min_std, mean_eval, max_std, max_eval, key)
            f.write(result)
            i += 1


def write(results):
    write_fitness(results, 'fit')
    write_eval(results, 'eval')
    log.info("DONE")
