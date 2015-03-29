# -*- coding: utf-8 -*-

'''
Boolean problem evaluator.
'''

from boolean import boolean, create_c_array
from ctypes import pointer, c_float, c_int


class Evaluator(object):

    def __init__(self):
        self.evaluations_number = 0

    def configure(self, config=''):
        self.boolean_type = int(config.boolean_type)
        boolean.eval.restype = c_float

    def evaluate(self, solution):
        self.evaluations_number += 1
        tt = create_c_array(solution)
        nVariables = c_int(8)
        varijanta = c_int(self.boolean_type)
        stop = c_int(0)
        sp = pointer(stop)
        return boolean.eval(tt, nVariables, varijanta, sp)
