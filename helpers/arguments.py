# -*- coding: utf-8 -*-

'''
Parser of the command line arguments.
'''

import sys
import logging

log = logging.getLogger(__name__)


def get_arg(name, default=None):
    '''
    Args:
        name: name of argument, e.g. -i, which may stands for
              input_path. The related variable has to be
              immediately after the argument name. Full
              example: python script.py -i input_path
              (input_path is, let say, an input file path).

        default: default value if the argument doesn't
                 exist.
    '''
    if name in sys.argv:
        return sys.argv[sys.argv.index(name) + 1]
    else:
        return default
