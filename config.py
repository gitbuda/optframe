# -*- coding: utf-8 -*-

'''
Config reader.
'''

import logging
import ConfigParser


def read(path):
    '''
    Reads settings file from .ini file
    and returns it as ConfigParser object
    '''

    logger = logging.getLogger(__name__)

    settings = ConfigParser.ConfigParser()

    settings.read(path)

    logger.info('Settings file reading: DONE')

    return settings
