#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The operator generates random permutation box.
'''

import random


class PermutationBoxOperator(object):

    def __init__(self, size):
        '''
        '''
        self.size = size

    def generate(self):
        '''
        '''
        box = [x for x in xrange(self.size)]
        random.shuffle(box)
        return box
