#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The operator generates random bit box.
'''

import random


class BitBoxOperator(object):

    def __init__(self, size):
        '''
        '''
        self.size = size

    def generate(self):
        '''
        '''
        box = [random.randint(0, 1) for x in xrange(self.size)]
        return box
