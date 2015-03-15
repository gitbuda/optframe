#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import uuid
import logging
import numpy as np

log = logging.getLogger(__name__)


def write(results):

    file_name = 'output/%s' % uuid.uuid4().hex
    with open(file_name, 'w') as f:
        f.write("problem, algorithm: min_fitness, max_fitness, mean_fitness\n")
        for key, value in results.items():
            min_fit = np.min(value)
            max_fit = np.max(value)
            mean_fit = np.mean(value)
            result = '%s: %s, %s, %s\n' % (key, min_fit, max_fit, mean_fit)
            f.write(result)

    log.info('All results saved')
