#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Discretize float range using the Gray code:
https://en.wikipedia.org/wiki/Gray_code.
Discretized float range is cached so an float
value hasn't be recalculated each time when
something needs that value.
'''


class BinaryToFloatCached(object):

    def __init__(self, bits, minimum, maximum):
        '''
        Calculates all descrete elements between,
        minimum and maximum values. Minimum value
        is included, maximum value is exculuded:
        [minimum, maximum>

        Args:
            bits:    number of bits, resolution
            minimum: interval minimum value
            maximum: interval maximum value
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
        '''
        Args:
            bit_array: array of bits

        Returns: float value related to a
                 bit_array value
        '''
        index = 0
        for bit in bit_array:
            index <<= 1
            index |= bit
        return self.values[index]


if __name__ == '__main__':

    b2f = BinaryToFloatCached(5, -5.12, 5.12)

    print "Values len: %s" % len(b2f.values)
    print "Values: %s" % b2f.values
    bit_array = [1, 1, 1, 1, 1]
    print "Conversion example: %s -> %s" % (bit_array, b2f.convert(bit_array))
