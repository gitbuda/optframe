#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Every evaluator has to return this object.
Fitness object has overridden comparison
operators so an algorithm can compare the
two fitness objects. E.g. if fitness1 >
fitness2 than the fitness1 is the better
one, although fitness2 could hold the
bigger value.
'''

import copy
import logging


log = logging.getLogger(__name__)

MAX_NAME = 'max'
MAX = 0  # grater fitness is better
MIN_NAME = 'min'
MIN = 1  # smaller fitness is better


def real_eq(a, b, epsilon=0.00000001):
    '''
    Equality of two real numbers a and b.
    '''
    return abs(a - b) < epsilon


class Fitness(object):
    '''
    Fitness categories(types):
        MIN == 1 -> grater fitness is better
        MAX == 0 -> smaller fitness is better
    '''

    def __init__(self, value=0, category=MAX):
        '''
        Args:
            value: some number
            category: fitness type
        '''
        self.value = value
        self.category = category

    def deep_copy(self):
        return copy.deepcopy(self)

    def __lt__(self, fitness):
        if self.category == MAX:
            return self.value < fitness.value
        else:
            return self.value > fitness.value

    def __le__(self, fitness):
        if self.__eq__(fitness):
            return True

        if self.category == MAX:
            return self.value < fitness.value
        else:
            return self.value > fitness.value

    def __eq__(self, fitness):
        return real_eq(self.value, fitness.value)

    def __ne__(self, fitness):
        return not self.__eq__(fitness)

    def __gt__(self, fitness):
        if self.category == MAX:
            return self.value > fitness.value
        else:
            return self.value < fitness.value

    def __ge__(self, fitness):
        if self.__eq__(fitness):
            return True

        if self.category == MAX:
            return self.value > fitness.value
        else:
            return self.value < fitness.value

    def __str__(self):
        '''
        String representation.
        '''
        if self.category == MIN:
            category_name = MIN_NAME
        else:
            category_name = MAX_NAME
        string = ''
        string += '{ '
        string += '\"category\": %s, ' % category_name
        string += '\"value\": %s' % str(self.value)
        string += ' }'
        return string
