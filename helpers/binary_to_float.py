#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Bit array to float array
'''

import logging

log = logging.getLogger(__name__)


class BinaryToFloatCached(object):

    def __init__(self, bits, minimum, maximum):
        '''
        TODO: gray code
        '''
        self.bits = bits
        self.minimum = minimum
        self.maximum = maximum
        self.length = 1 << self.bits
        self.values = [0 for i in xrange(self.length)]
        self.span = self.maximum - self.minimum
        for i in xrange(self.length):
            gray = (i >> 1) ^ i
            self.values[gray] = \
                i / float(self.length) * self.span + self.minimum

    def convert(self, bit_array):
        index = 0
        for bit in bit_array:
            index <<= 1
            index |= bit
        return self.values[index]


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    b2f = BinaryToFloatCached(5, -5.12, 5.12)

    log.info(len(b2f.values))
    log.info(b2f.values)
    log.info(b2f.convert([1, 1, 1, 1, 1]))
