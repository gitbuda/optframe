# -*- coding: utf-8 -*-

'''
Pipeline problem evaluator.
'''

from ctypes import cdll, c_int, c_float, c_char_p
import os

# load boolean library from current file folder
# boolean library name is libboolean.so
# create abs path to library
folder_path = os.path.split(os.path.abspath(__file__))[0]
pipeline_lib_path = os.path.join(folder_path, 'build/libpipeline.so')

# load library
pipeline = cdll.LoadLibrary(pipeline_lib_path)


def create_c_array(py_array):
    '''
        convert python array (py_array) into
        ctype array (c_array)
    '''
    c_array = (c_int * len(py_array))()
    for i in range(len(py_array)):
        c_array[i] = py_array[i]
    return c_array


class Evaluator(object):

    def __init__(self):
        self.evaluations_number = 0

    def configure(self, config=''):
        pipeline.load(c_char_p(config.pipeline_path))
        pipeline.evaluate.restype = c_float

    def evaluate(self, solution):
        self.evaluations_number += 1
        c_array = create_c_array(solution)
        cost = pipeline.evaluate(c_array, len(solution))
        return cost
