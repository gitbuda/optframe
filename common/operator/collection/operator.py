#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import random
import logging

from common.solution import Solution
import common.constants as CONST
from helpers.setter import setter

log = logging.getLogger(__name__)


class BitOperator(object):

    def configure(self, config):
        self.size = int(config.size)

    def generate(self):
        generated = [random.randint(0, 1) for x in xrange(self.size)]
        return generated


class PermutationOperator(object):

    def configure(self, config):
        self.size = int(config.size)

    def generate(self):
        box = [x for x in range(self.size)]
        random.shuffle(box)
        return box


class IntOperator(object):

    def configure(self, config):
        self.size = int(config.size)
        self.min = int(config.min)
        self.max = int(config.max)

    def generate(self):
        return [random.randint(self.min, self.max) for x in xrange(self.size)]

# TODO: FloatOperator


class Operator(object):

    def __init__(self):
        '''
        '''
        pass

    def configure(self, config):
        '''
        '''
        self.size = setter(
            lambda: int(config.collection_size), 20)
        self.solution_structure = config.solution_structure

        self.operators = {}

        # TODO: remove CP of code
        try:
            bit_operator = BitOperator()
            bit_operator.configure(self.solution_structure.bit)
            self.operators[CONST.BIT_BOX_KEY] = bit_operator
        except Exception:
            log.info("no bit box")

        try:
            perm_operator = PermutationOperator()
            perm_operator.configure(self.solution_structure.permutation)
            self.operators[CONST.PERMUTATION_BOX_KEY] = perm_operator
        except Exception:
            log.info("no permutation box")

        try:
            int_operator = IntOperator()
            int_operator.configure(self.solution_structure.int)
            self.operators[CONST.INT_BOX_KEY] = int_operator
        except Exception:
            log.info("no int box")

    def generate(self, size=None):
        '''
        '''
        if size is None:
            size = self.size

        collection = list()

        for index in range(size):
            solution = Solution({})
            for key in self.solution_structure.keys():
                solution.container[key] = self.operators[key].generate()
            collection.append(solution)

        return collection
