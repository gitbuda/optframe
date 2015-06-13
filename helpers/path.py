#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Path related stuff.
'''

import os
import uuid
import datetime
from os.path import join as path_join


def unique_name(prefix):
    '''
    Returns unique file name in format:
    prefix-uuid-time

    Args:
        prefix: file prefix
    '''
    file_uuid = uuid.uuid4().hex
    file_time = datetime.datetime.utcnow().strftime('%d-%m-%Y-%H-%M')
    return '%s-%s-%s' % (prefix, file_uuid, file_time)


def unique_path(folder, prefix):
    '''
    Returns relative path to a unique file name.

    Args:
        folder: relative path to the folder
        prefix: file name prefix
    '''
    return path_join(folder, unique_name(prefix))


def abs_path(file_path, file_name):
    '''
    Returns abs path to the file_name.

    Args:
        file_path: path to some file that is in the same folder
                   as file which path will be created
                   when this function is called this argument
                   could be e.g. __file__, in that case the function
                   will return /path/to/caller_file/file_name
                               -------------------- ---------
        file_name: file name
    '''
    folder_path = os.path.split(os.path.abspath(file_path))[0]
    return os.path.join(folder_path, file_name)


if __name__ == '__main__':

    # manual tests
    print unique_name('test')
    print unique_path('output', 'test')
    print abs_path(__file__, 'test.txt')
    print abs_path(__file__, unique_path('output', 'test'))
