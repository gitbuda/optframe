#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Class which purpose is to control an algorithm execution.

An object instantiated from this class has to be used in
with statement e.g.:
    with Limit(config):
        algorithm code block
config constructor parameter has to be dictionary wrapper
class.

TODO: finish docs

Execution limits:
    time_limit: N seconds
'''

import signal
import logging
from helpers.setter import setter
from common.exception.time_limit_exception import TimeLimitException

log = logging.getLogger(__name__)


# mock class
class Context(object):
    def __init__(self):
        self.time_limit = "10"


class Limit():

    def __init__(self, config=None):
        '''
        Arga:
            config -> limit configuration
        '''
        self.time_limit = setter(lambda: int(config.time_limit), None)

    def __enter__(self):
        '''
        Setup time limit timer.
        '''
        if self.time_limit is not None:
            signal.signal(signal.SIGALRM, self.raise_timeout)
            signal.alarm(self.time_limit)

    def __exit__(self, etype, evalue, etraceback):
        '''
        Catch exceptions produced in code block.
        '''
        signal.alarm(0)
        signal.signal(signal.SIGALRM, self.empty_timeout)
        if evalue is not None:
            log.info(evalue)
        # if all((etype, evalue, etraceback)):
        #     raise etype, evalue, etraceback
        import traceback
        traceback.print_exc()
        return True

    def raise_timeout(self, *args):
        '''
        Raise time limit exception, this method will be called
        on SIGALARM.
        '''
        raise TimeLimitException("time limit exceeded")

    def empty_timeout(self, *args):
        '''
        Empty method.
        '''
        pass

if __name__ == '__main__':

    context = Context()
    try:
        with Limit(context):
            i = 0
            while True:
                import time
                time.sleep(1)
                i += 1
                # if i == 5:
                #     raise Exception("some other limit")
                print i
    except Exception as e:
        print e
