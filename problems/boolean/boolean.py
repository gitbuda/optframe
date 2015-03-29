#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ctypes import cdll, c_int
import os

# load boolean library from current file folder
# boolean library name is libboolean.so
# create abs path to library
folder_path = os.path.split(os.path.abspath(__file__))[0]
boolan_lib_path = os.path.join(folder_path, 'libbool1.so')

# load library
boolean = cdll.LoadLibrary(boolan_lib_path)


def create_c_array(py_array):
    '''
        convert python array (py_array) into
        ctype array (c_array)
    '''
    c_array = (c_int * len(py_array))()
    for i in range(len(py_array)):
        c_array[i] = py_array[i]
    return c_array


if __name__ == '__main__':

    # basic example 
    # create python array
    booleans = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0]
    
    # call eval function from boolean library
    print boolean.eval(create_c_array(booleans), 4)
