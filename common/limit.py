#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
time_limit: N seconds
'''

import signal
import logging

from common.exception.time_limit_exception import TimeLimitException

log = logging.getLogger(__name__)


class Limit():

    def __init__(self, time_limit=None):
        '''
        '''
        self.time_limit = time_limit

    def __enter__(self):
        '''
        '''
        if self.time_limit is not None:
            signal.signal(signal.SIGALRM, self.raise_timeout)
            signal.alarm(self.time_limit)

    def __exit__(self, etype, evalue, etraceback):
        '''
        '''
        signal.alarm(0)
        signal.signal(signal.SIGALRM, self.empty_timeout)

    def raise_timeout(self, *args):
        '''
        '''
        raise TimeLimitException("time_limit exceeded")

    def empty_timeout(self, *args):
        '''
        '''
        pass
