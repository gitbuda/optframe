# -*- coding: utf-8 -*-

'''
LimitException is used when some kind of limit
is reached.

Kind of limits are:

    iteration_limit -> max number of algorithm iterations,
        every algorithm defines what is one iteration

    evaluation_limit -> max number of evaluations

    time_limit -> algorithm execution time max

    memory_limit -> algorithm memory consumption max

    fitness_limit -> best fitness value for the given
        problem, every problem defines what is fitness
        limit
'''


class LimitException(Exception):
    '''
    '''
    pass
