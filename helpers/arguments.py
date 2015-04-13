#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import sys
import logging

log = logging.getLogger(__name__)


def get_arg(name, default=None):
    '''
    '''
    if name in sys.argv:
        return sys.argv[sys.argv.index(name) + 1]
    else:
        return default
