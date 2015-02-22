# -*- coding: utf-8 -*-

'''
Boolean problem evaluator.
'''

from boolean.boolean import boolean, create_c_array


class BoolArrayEvaluator(object):

    def __init__(self):
        pass

    def evaluate(self, genotype):
        c_array = create_c_array(genotype)
        return boolean.eval(c_array, 8)
