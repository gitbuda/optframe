#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Module returns a process memory usage.
'''

import os
import psutil


unit_container = {}
unit_container['KiB'] = float(2 ** 10)
unit_container['MiB'] = float(2 ** 20)
unit_container['GiB'] = float(2 ** 30)
unit_container['TiB'] = float(2 ** 40)


def memory_usage(pid, unit='GiB'):
    '''
    '''
    process = psutil.Process(pid)
    mem = process.get_memory_info()[0] / unit_container[unit]
    return mem


def self_memory_usage(unit='GiB'):
    '''
    '''
    return memory_usage(os.getpid(), unit)


if __name__ == '__main__':

    a = [0] * (2 ** 27)
    unit = 'GiB'
    print('Memory usage: %s%s' % (self_memory_usage(unit), unit))
