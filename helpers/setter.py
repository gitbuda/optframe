#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

log = logging.getLogger(__name__)


def setter(value, default):
    '''
    '''
    try:
        return value()
    except Exception:
        return default
