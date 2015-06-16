#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The purpose of this script is to build grid search elements container.
'''

import itertools

from helpers.dict_wrapper import DictWrapper


def create_item(keys, values):
    '''
    Creates one grid element.

    Args:
        keys:   all grid element keys
        values: all grid element values
    '''
    item = {}
    for index, key in enumerate(keys):
        item[key] = values[index]
    return DictWrapper(item)


def grid_item_container(grid_config):
    '''
    Creates grid search elements container.

    Args:
        grid_config: DictWrapper instance whare
                     all values are arrays.

    Returns:
        list of DictWrapper objects (grid search elements)
    '''
    grid_keys = grid_config.keys()
    lists = []
    for key in grid_keys:
        lists.append(grid_config[key])
    grid = [create_item(grid_keys, grid_element)
            for grid_element in itertools.product(*lists)]
    return grid


if __name__ == '__main__':

    grid = grid_item_container(DictWrapper({'x': [1, 2], 'y': [3, 4]}))
    for grid_element in grid:
        print grid_element
        print '---------------------'
