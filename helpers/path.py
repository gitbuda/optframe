#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import uuid
import datetime
import logging

from os.path import join as path_join

log = logging.getLogger(__name__)


def unique_path(folder, prefix):
    '''
    '''
    path_format = path_join('%s', '%s-%s-%s')
    unique_path = path_format % \
        (folder,
         prefix,
         uuid.uuid4().hex,
         datetime.datetime.utcnow().strftime('%d-%m-%Y-%H-%M'))
    return unique_path


if __name__ == '__main__':
    pass
