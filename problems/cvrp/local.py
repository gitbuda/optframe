#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
CVRP local search.
'''

import sys
from itertools import permutations
from common.solution import Solution
from helpers.dict_wrapper import DictWrapper
from problems.cvrp.evaluator import Evaluator
from problems.cvrp.hmo_output import read, write
from problems.cvrp.hmo_loader import read_hmo_file


def calc_distance(problem, warehouse, bucket):
    dist = 0
    dist += problem.wcdistances[warehouse][bucket[0]]
    if len(bucket) == 1:
        return 2 * dist
    else:
        dist += problem.wcdistances[warehouse][bucket[-1]]
    for first, second in zip(bucket[:-1], bucket[1:]):
        dist += problem.ccdistances[first][second]
    return dist


if __name__ == '__main__':

    # read input parameters
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # read initial solution
    solution = read(input_path)
    ws = solution.container['int']
    cs = solution.container['permutation']

    # read problem
    hmo_problem = read_hmo_file('input.txt')

    # improve solution
    warehouses = [ws[0] - 1]
    customers = [[cs[0]]]
    for warehouse, customer in zip(ws[1:], cs[1:]):
        if warehouse != 0:
            warehouses.append(warehouse - 1)
            customers.append([])
        customers[-1].append(customer)

    icustomers = []
    for warehouse, bucket in zip(warehouses, customers):
        distances = []
        perms = list(permutations(bucket))
        for perm in perms:
            distances.append(calc_distance(hmo_problem, warehouse, perm))
        min_perm = perms[distances.index(min(distances))]
        icustomers.append(min_perm)

    int_box = []
    perm_box = []
    for warehouse, customers in zip(warehouses, icustomers):
        int_box += [warehouse + 1] + [0] * (len(customers) - 1)
        perm_box += customers

    # write founded solution
    solution = Solution({'int': int_box, 'permutation': perm_box})
    evaluator = Evaluator()
    evaluator.configure(DictWrapper({'path': 'input.txt'}))
    fitness = evaluator.evaluate(solution)
    solution.fitness = fitness
    write(output_path, solution)
