# -*- coding: utf-8 -*-

'''
Leading ones problem evaluator.
e.g.
[1, 1, 0, 1, 1] -> 2 -> (normalized) -> 0.4
'''


class Evaluator(object):

    def __init__(self):
        self.evaluations_number = 0

    def configure(self, config=''):
        pass

    def evaluate(self, solution):
        '''
        Calculates normalized sum of leading ones
        in a bit string solution.
        If this function receive solution that is not
        a bit string it will return wrong value (1.0).
        Bitstring check operation is expensive and here
        isn't a place where this should be chacked.
        '''
        self.evaluations_number += 1
        ones = 0
        for bit in solution:
            if bit != 1:
                break
            ones += bit
        return 1.0 * ones / len(solution)
