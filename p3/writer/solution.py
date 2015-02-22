# -*- coding: utf-8 -*-

'''
Solution writer
'''


class SolutionWriter(object):

    def __init__(self):
        pass

    def write(self, path, array, fitness):
        with open(path, 'w') as f:
            f.write(" ".join([str(n) for n in array]))
            f.write("\n")
            f.write(str(fitness))
