# -*- coding: utf-8 -*-

'''
Onemax problem evaluator.
'''


class Evaluator(object):

    def __init__(self):
        self.evaluations_number = 0

    def configure(self, config=''):
        pass

    def evaluate(self, solution):
        self.evaluations_number += 1
        gene_sum = float(sum(solution))
        return gene_sum / len(solution)
