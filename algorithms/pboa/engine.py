#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

from common.best_store import BestStore

log = logging.getLogger(__name__)


def run(context):
    '''
    '''
    # e.g.
    # solution_size = context.solution_size
    # evaluator = context.evaluate_operator

    best_store = BestStore()
    best_store.configure(context.config)

    try:
        pass
    except Exception:
        pass

    return (best_store.best_solution, best_store.best_fitness)


if __name__ == '__main__':
    pass
