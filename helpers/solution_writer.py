# -*- coding: utf-8 -*-

'''
Solution writer
'''

import json


class SolutionWriter(object):

    def __init__(self):
        pass

    def write(self, path, solution):
        data = {}
        data['fitness'] = solution.fitness.value
        data['container'] = list(solution.container)
        with open(path, 'w') as f:
            json.dump(data, f)
