# -*- coding: utf-8 -*-

'''
Used for setup a some kind of value.

If values is not set, than the default value
has to be returned.
'''

import logging

log = logging.getLogger(__name__)


def setter(value, default):
    '''
    Args:
        value:   lambda function which returns a value
        default: default value which is returned if an
                 error occurres in the lambda function
    '''
    try:
        return value()
    except Exception:
        return default
