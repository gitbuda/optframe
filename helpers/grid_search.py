#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging
import itertools

from helpers.loader import DictWrapper

log = logging.getLogger(__name__)


def create_item(keys, values):
    '''
    '''
    item = {}
    for index, key in enumerate(keys):
        item[key] = values[index]
    return DictWrapper(item)


def grid_item_container(grid_config):
    '''
    '''
    grid_keys = grid_config.keys()
    lists = []
    for key in grid_keys:
        lists.append(grid_config[key])
    grid = [create_item(grid_keys, grid_element)
            for grid_element in itertools.product(*lists)]
    return grid


if __name__ == '__main__':
    pass
