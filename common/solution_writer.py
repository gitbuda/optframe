# -*- coding: utf-8 -*-

'''
Algorithm local solution writer.
'''

import uuid


def write(solution, path, identifier=None):
    fitness = solution.fitness.value
    unique = uuid.uuid4().hex
    if identifier is None:
        path_template = '%s/f_%s-%s.solution'
        output_path = path_template % (path, fitness, unique)
    else:
        path_template = '%s/id_%s-f_%s-%s.solution'
        output_path = path_template % (path, identifier, fitness, unique)
    solution.persist(output_path)
