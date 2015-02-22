# -*- coding: utf-8 -*-

import sys
from boolean.boolean import boolean, create_c_array

tsp_distances = []
with open('bays29.tsp') as f:
    lines = f.readlines()
    for line in lines:
        row = [int(x) for x in line.rstrip().split(' ') if x]
        tsp_distances.append(row)


def tsp_evaluate(genotype):

    cost = 0
    length = len(genotype)
    unique = set()

    for i, item in enumerate(genotype):

        if item in unique:
            return -sys.maxsize

        if i + 1 == length:
            next_item = 0
        else:
            next_item = genotype[i + 1]

        unique.add(item)

        cost += tsp_distances[item][next_item]

    return -cost


def sbox_evaluate(genotype):
    c_array = create_c_array(genotype)
    return boolean.eval(c_array, 8)
