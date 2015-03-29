#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging


def print_matrix(matrix):
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix[0])):
            line += ("%.2f" % float(matrix[i][j])) + " "
        print(line)

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
