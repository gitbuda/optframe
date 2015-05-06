#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Calculate distances between points in 2D space.

Points are loaded from file which path is specified
as first argument. File format is:
1 x y
2 x y
3 x y
...
'''

import sys
from math import sqrt
import logging

log = logging.getLogger(__name__)

if __name__ == '__main__':

    path = sys.argv[1]

    data = {}
    with open(path, 'r') as f:
        lines = f.readlines()
        for point in lines:
            point = point.rstrip().split('\t')
            data[int(point[0]) - 1] = (float(point[1]), float(point[2]))

    size = len(data)
    matrix = ''
    for i in range(size):
        line = ''
        for j in range(size):
            if i == j:
                line += ' 0.0000'
            else:
                x, y = data[i], data[j]
                line += ' %.4f' % sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
        line += '\n'
        matrix += line
    print matrix
