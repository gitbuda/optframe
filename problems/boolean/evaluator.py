# -*- coding: utf-8 -*-

'''
Boolean problem evaluator.
'''

from boolean import boolean, create_c_array
from ctypes import pointer, c_float, c_int
from common.evaluation_counter import EvaluationCounter
from common.fitness import Fitness, MAX
from common.constants import BIT_BOX_KEY


class Evaluator(object):

    def __init__(self):
        '''
        '''
        self.evaluation_counter = EvaluationCounter()

    def configure(self, config=''):
        '''
        '''
        self.boolean_type = int(config.boolean_type)
        boolean.eval.restype = c_float
        self.evaluation_counter.configure(config)

    def evaluate(self, solution):
        '''
        '''
        self.evaluation_counter.increment()

        tt = create_c_array(solution.container[BIT_BOX_KEY])
        nVariables = c_int(8)
        varijanta = c_int(self.boolean_type)
        stop = c_int(0)
        sp = pointer(stop)

        return Fitness(boolean.eval(tt, nVariables, varijanta, sp), MAX)
