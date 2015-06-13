#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
convert Solution txt file into output file
'''

import sys
from common.fitness import Fitness, MIN
from common.solution import Solution
from helpers.dict_wrapper import load_json
from problems.cvrp.hmo_output import write


def format(input_path, output_path):
    '''
    reads input path and writes to the output path
    '''
    solution_dict = load_json(input_path)
    solution = Solution({'int': solution_dict.int,
                         'permutation': solution_dict.permutation})
    solution.fitness = Fitness(int(solution_dict.fitness), MIN)
    write(output_path, solution)


if __name__ == '__main__':

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    format(input_path, output_path)
