#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import uuid
import logging
import datetime
import numpy as np

log = logging.getLogger(__name__)


def write(results):

    file_name = 'output/%s-%s' % \
        (uuid.uuid4().hex,
         datetime.datetime.utcnow().strftime('%d-%m-%Y-%H-%M'))
    with open(file_name, 'w') as f:
        f.write("problem, algorithm: min_fitness, max_fitness, mean_fitness, min_evo, max_evo, mean_evo\n")
        for key, result in results.items():
            min_fit = np.min(result.fitness_container)
            max_fit = np.max(result.fitness_container)
            mean_fit = np.mean(result.fitness_container)
            min_evo = np.min(result.evaluations_container)
            max_evo = np.max(result.evaluations_container)
            mean_evo = np.mean(result.evaluations_container)
            result = '%s: %s, %s, %s, %s, %s, %s\n' % (key, min_fit, max_fit, mean_fit, min_evo, max_evo, mean_evo)
            f.write(result)

    log.info('All results saved')
