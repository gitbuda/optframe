# -*- coding: utf-8 -*-

'''
Algorithm local solution writer.
'''

import uuid


def write(solution, path):
    fitness = solution.fitness.value
    output_path = '%s/f%s-%s.solution' % (path,
                                          fitness,
                                          uuid.uuid4().hex)
    solution.persist(output_path)
