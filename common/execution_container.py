# -*- coding: utf-8 -*-

'''
The object instantiated from this class contains
dictionary of ExecutionResult objects.
'''


class ExecutionContainter(object):

    def __init__(self):
        '''
        common_identifier is name of one execution
        '''
        self.common_identifier = None
        self.results = {}
        self.problem_variants = set()
