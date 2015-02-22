#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import sys


size_x = 5
size_y = 5
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


def print_matrix(matrix):
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix[0])):
            line += ("%.2f" % float(matrix[i][j])) + " "
        print(line)


def build_clusters(initial_distances):

    # initialize number of elements
    length = len(initial_distances)

    # initial_distances = init_distances()
    # print_matrix(initial_distances)

    usable = [i for i in range(length)]
    random.shuffle(usable)

    # clusters initialization
    # space for all possible clusters
    # upgma results with tree structure
    # so total number of clusters is 2 * length - 1
    clusters = [[]] * (2 * length - 1)

    # every element is at the beginning separated cluster
    for i in range(length):
        clusters[i] = [i]

    # useful = [1 for i in range(len(clusters))]

    distances = [[0] * len(clusters)] * len(clusters)

    for i in range(length - 1):
        for j in range(i, length):
            distances[i][j] = initial_distances[i][j]
            distances[j][i] = distances[i][j]

    index = len(usable) - 1
    while len(usable) > 0:
        min_distance = sys.float_info.max
        min_first = 0
        min_second = 0
        for i in range(0, len(usable) - 1):
            for j in range(i, len(usable)):
                first = usable[i]
                second = usable[j]
                if first == second:
                    continue
                current_distance = distances[first][second]
                if current_distance < min_distance:
                    min_distance = current_distance
                    min_first = first
                    min_second = second
        first_cluster = clusters[min_first]
        second_cluster = clusters[min_second]
        index += 1

        if index < len(clusters) - 1:
            usable.append(index)

        usable.remove(min_first)
        usable.remove(min_second)
        clusters[index] = first_cluster + second_cluster
        for j in range(len(usable) - 1):
            i = usable[j]
            first_element_d = 1.*distances[min_first][i]*len(first_cluster)
            second_element_d = 1.*distances[min_second][i]*len(second_cluster)
            sum_element_d = first_element_d + second_element_d
            sum_length = len(first_cluster) + len(second_cluster)
            i_to_new = sum_element_d + sum_length
            distances[i][index] = i_to_new
            distances[index][i] = i_to_new

    # TODO: different cluster ordering (random, length, etc)
    important_clusters = clusters[length:2*length - 2]
    return (important_clusters, distances)

if __name__ == "__main__":
    distances = init_distances()
    (clusters, distances) = build_clusters(distances)
    print clusters
