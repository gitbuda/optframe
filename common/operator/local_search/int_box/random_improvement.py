#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

# import random
import logging
# from common.constants import INT_BOX_KEY

log = logging.getLogger(__name__)


class LocalSearch(object):

    def configure(self, context):
        '''
        Configure the random improvement local search.

        Args:
            context: execution context
        '''
        self.evaluator = context.evaluate_operator
        return self

    def search(self, solution):
        '''
        The random improvement search.

        Args:
            solution: instance of the Solution class
        '''
        # TODO: impementation

        return solution


if __name__ == '__main__':

    class Evaluator():
        def evaluate(self, solution):
            return 0

    class Context():
        pass

    from common.solution import Solution
    context = Context()
    context.evaluate_operator = Evaluator()
    local = LocalSearch()
    local.configure(context)
    local.search(Solution({"permutation": [2, 3, 1, 5, 4]}, 0))
