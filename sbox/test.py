#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from ctypes import cdll, c_int
import random

# load boolean library from current file folder
# boolean library name is libboolean.so
# create abs path to library
folder_path = os.path.split(os.path.abspath(__file__))[0]
transparency_lib_path = os.path.join(folder_path, 'libtransparency.so')

# load library
transparency = cdll.LoadLibrary(transparency_lib_path)

# float eval(u8 tt[N][256], bool& stop)


def create_c_array(py_array):
    '''
        convert python array (py_array) into a
        ctype array (c_array)
    '''
    c_array = (c_int * len(py_array))()
    for i in range(len(py_array)):
        c_array[i] = py_array[i]
    return c_array


if __name__ == '__main__':

    # basic example
    # create python array
    length = 256
    t_length = 8
    permutations = [x for x in range(length)]
    random.shuffle(permutations)
    tt = [[0] * length for x in range(t_length)]

    print tt
    for i in range(length):
        for j in range(t_length):
            tt[j][i] = permutations[i] >> (7 - j) & 0x01

