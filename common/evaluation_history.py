# -*- coding: utf-8 -*-

'''
The object instantiated from this class contains
solutions in one execution.
'''

from helpers.setter import setter


class EvaluationHistory(object):

    def configure(self, config):
        '''
        '''
        self.history = []
        self.evaluation_history = setter(
            lambda: config.evaluation_history, None)
        if self.evaluation_history is not None:
            if self.evaluation_history.type == 'linear':
                self.event_point = int(self.evaluation_history.precision)
            elif self.evaluation_history.type == 'log':
                self.event_point = 10 ** int(self.evaluation_history.precision)
            else:
                self.event_point = None
        return self

    def save(self, counter, solution):
        '''
        '''
        if self.evaluation_history is not None \
           and self.event_point is not None:
            if counter % self.event_point == 0:
                self.history.append(solution)
