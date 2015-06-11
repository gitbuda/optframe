#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
            warehouses += [warehouse_index] + [-1] * (len(customer_indices)-1)
            customers += customer_indices
            f.readline()

        return warehouses + customers


def write(path, genotype, cost):

    half_size = len(genotype) / 2

    cluster_list = []
    warehouses = []
    clusters = []

    for i in range(half_size):
        if genotype[i] != -1:
            if len(cluster_list) != 0:
                clusters.append(cluster_list)
            cluster_list = [genotype[i + half_size]]
            warehouses.append(genotype[i])
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

if __name__ == '__main__':

    print read('res-slivar.txt')

    # write("nekaj.txt", [1, -1, -1, -1, 2, 3, -1, -1, 4, -1, 1, 2, 3, 4,5,6,7, 8, 9, 10], 300)
    write('341771', [4, -1, -1, -1, 3, -1, 4, -1, -1, -1, 3, -1, -1, -1, -1, 4, -1, -1, -1, 1, -1, -1, 3, -1, -1, -1, 4, 4, -1, -1, -1, 4, -1, -1, -1, 3, -1, -1, -1, 4, -1, -1, -1, 4, -1, -1, -1, 4, -1, -1, 1, -1, -1, -1, 3, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 3, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 3, -1, -1, -1, 4, -1, -1, -1, 1, 1, -1, -1, -1, -1, 4, 4, -1, -1, -1, 4, 92, 25, 15, 69, 47, 78, 79, 34, 63, 66, 53, 76, 4, 36, 65, 98, 61, 5, 82, 46, 84, 90, 83, 39, 94, 30, 12, 22, 64, 81, 14, 73, 18, 93, 95, 62, 77, 88, 8, 86, 87, 74, 60, 17, 32, 20, 70, 23, 49, 42, 67, 58, 71, 31, 48, 35, 56, 27, 85, 96, 40, 0, 13, 52, 97, 9, 72, 19, 45, 57, 28, 51, 3, 7, 11, 26, 75, 38, 50, 1, 29, 54, 68, 33, 44, 99, 41, 21, 16, 43, 80, 91, 89, 6, 59, 55, 2, 37, 10, 24], 341771)
