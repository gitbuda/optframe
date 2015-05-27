#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Parser of command line arguments.
'''

import sys
import logging

log = logging.getLogger(__name__)


def get_arg(name, default=None):
    '''
    Args:
        name: name of argument, e.g. -i, which stands for
              input_file, the related variable has to be
              after the argument name/flag, -i input_path
              (input_path is, let say, input file path)
        default: default value if the argument doesn't
                 exist
    '''
    if name in sys.argv:
        return sys.argv[sys.argv.index(name) + 1]
    else:
        return default
