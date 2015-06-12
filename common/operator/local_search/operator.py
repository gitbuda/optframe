#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Solution local search operator
'''

import logging
from common.constants import BIT_BOX_KEY
from common.constants import PERMUTATION_BOX_KEY
from common.constants import INT_BOX_KEY
from helpers.dict_wrapper import DictWrapper
from .bit_box.binary_tournament import LocalSearch as BinaryTournament
from .bit_box.first_improvement import LocalSearch as FirstImprovement
from .permutation_box.block_full import LocalSearch as BlockFull
from .permutation_box.bubble import LocalSearch as BubbleSearch
from .int_box.random_improvement import LocalSearch as RandomImprovement

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
        try:
            self.local_search = context.config.local_search
        except Exception:
            default = {
                'bit': {'name': 'first_improvement'},
                'permutation': {'name': 'block_full'},
                'int': {'name': 'random_improvement'}
            }
            self.local_search = DictWrapper(default)

        # TODO: dynamic implementation
        self.operators = {}
        self.operators[BIT_BOX_KEY] = {}
        self.operators[PERMUTATION_BOX_KEY] = {}
        self.operators[INT_BOX_KEY] = {}

        binary_tournament = BinaryTournament()
        binary_tournament.configure(context)
        self.operators[BIT_BOX_KEY]['binary_tournament'] = binary_tournament

        first_improvement = FirstImprovement()
        first_improvement.configure(context)
        self.operators[BIT_BOX_KEY]['first_improvement'] = first_improvement

        block_full = BlockFull()
        block_full.configure(context)
        self.operators[PERMUTATION_BOX_KEY]['block_full'] = block_full

        bubble = BubbleSearch()
        bubble.configure(context)
        self.operators[PERMUTATION_BOX_KEY]['bubble'] = bubble

        random_improvement = RandomImprovement().configure(context)
        self.operators[INT_BOX_KEY]['random_improvement'] = random_improvement

    def search(self, solution):
        '''
        '''
        for box in solution.container:
            name = self.local_search[box].name
            solution = self.operators[box][name].search(solution)

        return solution


if __name__ == '__main__':
    pass
