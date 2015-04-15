#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging
import itertools
from helpers.loader import DictWrapper

log = logging.getLogger(__name__)


def create_item(keys, values):
    item = {}
    for index, key in enumerate(keys):
        item[key] = values[index]
    return DictWrapper(item)


def execute(algorithms, problems, config):
    '''
    '''
    # create grid
    grid = config.grid
    grid_keys = grid.keys()
    lists = []
    for key in grid_keys:
        lists.append(grid[key])
    grid = [create_item(grid_keys, grid_element)
            for grid_element in itertools.product(*lists)]

    context = config.common
    for element in grid:
        context.hard_merge(element)
        log.info(context)
