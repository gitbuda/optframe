# -*- coding: utf-8 -*-

'''
Solution writer
'''

import json


class SolutionWriter(object):

    def __init__(self):
        pass

    def write(self, path, genes, fitness):
        data = {}
        data['fitness'] = fitness
        data['genes'] = list(genes)
        with open(path, 'w') as f:
            json.dump(data, f)
