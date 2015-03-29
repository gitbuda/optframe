#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random

import numpy as np
import scipy.cluster.hierarchy as hierarchy

size_x = 10
size_y = 10
vector = [i for i in range(size_x)]


# TODO: load from file
def init_distances():
    distances = [[0 for i in range(size_x)] for j in range(size_y)]
    for i in range(size_x):
        for j in range(size_y):
            if i == j:
                distances[i][j] = 0
            else:
                distances[i][j] = random.randint(1, size_x)
    return distances


def to_np_array(matrix):
    array = []
    size = len(matrix)
    for row in matrix:
        for elem in row:
            array.append(float(elem))
    return np.array(array).reshape((size, size))


def build(initial_distances):

    distances = to_np_array(initial_distances)
    sci_clusters = hierarchy.average(distances)
    clusters = [[i] for i in range(len(initial_distances))]

    for cluster in sci_clusters:
        first_index = int(cluster[0])
        first = clusters[first_index]
        second_index = int(cluster[1])
        second = clusters[second_index]
        clusters.append(first + second)

    return clusters[:-1]

if __name__ == "__main__":

    distances = init_distances()
    clusters = build(distances)
    print clusters
