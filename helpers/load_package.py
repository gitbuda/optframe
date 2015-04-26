#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import imp
import logging

from os import walk

log = logging.getLogger(__name__)


def load_package(path, tag='Module'):
    '''
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
            log.info(e)
    return package
