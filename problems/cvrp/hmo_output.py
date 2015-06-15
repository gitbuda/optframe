# -*- coding: utf-8 -*-

from common.solution import Solution


def read(path):

    with open(path) as f:
        lines_no = int(f.readline().rstrip('\r\n'))
        f.readline()

        warehouses = []
        customers = []
        for i in range(lines_no):
            line = str(f.readline().rstrip('\r\n'))
            splitted = line.split(':')
            warehouse_index = int(splitted[0])
            customer_indices = [int(x) for x in
                                splitted[1].lstrip(' ').split(' ')]
            warehouses += [warehouse_index + 1] + [0]*(len(customer_indices)-1)
            customers += customer_indices
            f.readline()

        return Solution({'int': warehouses, 'permutation': customers})


def write(path, solution):

    genotype = solution.container['int'] + solution.container['permutation']
    cost = solution.fitness.value

    half_size = len(genotype) / 2

    cluster_list = []
    warehouses = []
    clusters = []

    for i in range(half_size):
        if genotype[i] != 0:
            if len(cluster_list) != 0:
                clusters.append(cluster_list)
            cluster_list = [genotype[i + half_size]]
            warehouses.append(genotype[i] - 1)
        else:
            cluster_list.append(genotype[i + half_size])
        if i == half_size - 1:
            clusters.append(cluster_list)

    with open(path, 'w') as f:
        f.write('%d\r\n\r\n' % len(clusters))
        for i, warehouse in enumerate(warehouses):
            f.write('%d:' % warehouse)
            for j, customer in enumerate(clusters[i]):
                f.write(' %d' % customer)
            f.write('\r\n\r\n')
        f.write('\r\n\r\n')
        f.write('%d\r\n' % cost)
