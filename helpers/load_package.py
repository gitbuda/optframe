# -*- coding: utf-8 -*-

'''
Load all modules from a package.
'''

import imp
import logging
from os import walk

log = logging.getLogger(__name__)


def load_package(path, tag='Module'):
    '''
    Loads all modules at the path, if it is possible. If a
    module can't be loaded it will be skipped (only an exception
    message will be logged).
    '''
    package = {}
    (_, module_names, _) = walk(path).next()
    for module_name in module_names:
        try:
            f, filename, desc = imp.find_module(module_name, [path])
            modul = imp.load_module(module_name, f, filename, desc)
            package[module_name] = modul
            log.info('%s: %s loaded.', tag, module_name)
        except Exception as e:
            import traceback
            traceback.print_exc()
            log.info(e)
    return package
