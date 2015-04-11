#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    EvaluationsCounter

    Every algorithm could have evaluations number limit.
    If algorithm has evaluations number limit, this counter will
    throw evaluatior exception and an algorithm has return
    best solution so far.
'''

from common.exception.evaluator_exception import EvaluatorException


class EvaluationCounter(object):

    def __init__(self):
        '''
        Initialize evaluations number.
        '''
        self.evaluations_number = 0

    def configure(self, config):
        '''
        Initialize max evaluations number. If the config
        contains evaluations_number property take it as
        max_evaluations_number, else max evaluations number is
        None and EvaluatorException will never be thrown.
        '''
        try:
            self.max_evaluations_number = config.evaluations_number
        except KeyError:
            self.max_evaluations_number = None

    def increment(self):
        '''
        Increment the evaluations_number if becomes grater than
        max_evaluations_number EvaluatorException will be thrown
        because the execution of algorithm has to stop.
        '''
        self.evaluations_number += 1

        if self.max_evaluations_number is not None and \
           self.evaluations_number > self.max_evaluations_number:
            self.evaluations_number = self.max_evaluations_number
            raise EvaluatorException('Maximum number of evaluations exceeded')
