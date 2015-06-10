#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Object which purpose is to pass solutions between algorithms.
'''

from common.solution import Solution


class SolutionBuffer(object):

    def __init__(self):
        '''
        Initialize the buffer.
        '''
        self.buffer = []

    def configure(self, config):
        '''
        Configure the buffer. Buffer size, solution type...
        '''
        return self

    def writeone(self, solution):
        '''
        Add the solution to the buffer.
        '''
        self.buffer.append(solution)

    def writeall(self, solutions):
        '''
        Add the solutions to the buffer.
        '''
        self.buffer += solutions

    def readone(self):
        '''
        Returns the first solution and remove
        it from the buffer.
        If buffer has no solutions return a random
        solution.
        '''
        if len(self.buffer) > 0:
            return self.buffer.pop(0)
        else:
            return Solution({})

    def readall(self):
        '''
        '''
        if len(self.buffer) > 0:
            solutions = self.buffer
            self.buffer = []
            return solutions
        else:
            return [Solution({})]


if __name__ == '__main__':
    sb = SolutionBuffer()
    sb.writeone(Solution({}))
    s1 = sb.readone()
    print s1
    s2 = sb.readone()
    print s2
    sb.writeall([Solution({}), Solution({})])
    print sb.readall()
    print sb.readone()
    print sb.readall()
