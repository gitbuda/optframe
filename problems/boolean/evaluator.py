# -*- coding: utf-8 -*-

'''
Boolean problem evaluator.
'''

from boolean import boolean, create_c_array


class Evaluator(object):

    def __init__(self):
        pass

    def configure(self, config=''):
        pass

    def evaluate(self, solution):
        c_array = create_c_array(solution)
        return boolean.eval(c_array, 8)
