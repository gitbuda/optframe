#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Solution local search operator
'''

import logging
from common.constants import BIT_BOX_KEY
from common.constants import PERMUTATION_BOX_KEY
from .bit_box.binary_tournament import LocalSearch as BinaryTournament
from .bit_box.first_improvement import LocalSearch as FirstImprovement
from .permutation_box.block_full import LocalSearch as BlockFull

log = logging.getLogger(__name__)


class Operator(object):

    def __init__(self):
        '''
        '''
        pass

    def configure(self, context):
        '''
        '''
        self.evaluator = context.evaluate_operator
        self.local_search = context.config.local_search

        self.operators = {}
        self.operators[BIT_BOX_KEY] = {}
        self.operators[PERMUTATION_BOX_KEY] = {}

        binary_tournament = BinaryTournament()
        binary_tournament.configure(context)
        self.operators[BIT_BOX_KEY]['binary_tournament'] = binary_tournament

        first_improvement = FirstImprovement()
        first_improvement.configure(context)
        self.operators[BIT_BOX_KEY]['first_improvement'] = first_improvement

        block_full = BlockFull()
        block_full.configure(context)
        self.operators[PERMUTATION_BOX_KEY]['block_full'] = block_full

    def search(self, solution):
        '''
        '''
        for box in solution.container:
            name = self.local_search[box].name
            solution = self.operators[box][name].search(solution)

        return solution


if __name__ == '__main__':
    pass
