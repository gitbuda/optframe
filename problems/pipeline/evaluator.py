# -*- coding: utf-8 -*-

'''
Pipeline problem evaluator.
'''

import os

from ctypes import cdll, c_int, c_float, c_char_p
from common.evaluation_counter import EvaluationCounter
from common.fitness import Fitness, MIN
from common.constants import BIT_BOX_KEY

# find c pipeline library
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
        '''
        '''
        self.evaluation_counter = EvaluationCounter()

    def configure(self, config=''):
        '''
        '''
        self.evaluation_counter.configure(config)
        pipeline.load(c_char_p(config.pipeline_path))
        pipeline.evaluate.restype = c_float

    def evaluate(self, solution):
        '''
        '''
        self.evaluation_counter.increment()
        solution = solution.container[BIT_BOX_KEY]

        c_array = create_c_array(solution)
        cost = pipeline.evaluate(c_array, len(solution))

        return Fitness(cost, MIN)
