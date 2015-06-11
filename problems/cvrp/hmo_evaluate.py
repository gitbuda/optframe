#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import sys
from hmo_loader import read_hmo_file
from common.solution import Solution


class Evaluator(object):

    def __init__(self, path):
        self.hmo_problem = read_hmo_file(path)
        self.hmo_problem.calculate_distances()

    def configure(self, config):
        pass

    def evaluate(self, solution):
        '''
        '''

        warehouses_indices = solution.container['int']
        customers_indices = solution.container['permutation']

        if warehouses_indices[0] == 0:
            return sys.maxint

        cost = 0

        customers_no = self.hmo_problem.customers_no

        # groupes
        groupes = []
        current = warehouses_indices[0]
        counter = 1
        start = 0
        for i in range(0, customers_no):
            if i + 1 == customers_no or warehouses_indices[i + 1] != 0:
                groupes.append((current, start, counter))
                if i + 1 != customers_no:
                    current = warehouses_indices[i + 1]
                    counter = 1
                    start = i + 1
            else:
                counter += 1
        ######################################

        # check warehouses constraints
        warehouses_constraints = list(self.hmo_problem.warehouse_capacities)
        used_warehouses = set()
        for groupe in groupes:
            cost += self.hmo_problem.vehicle_price
            warehouse_index = groupe[0]
            used_warehouses.add(warehouse_index)
            start = groupe[1]
            count = groupe[2]
            sub_perm = customers_indices[start:start + count]

            cost += self.hmo_problem.wcdistances[warehouse_index][sub_perm[0]]
            cost += self.hmo_problem.wcdistances[warehouse_index][sub_perm[-1]]

            sub_perm_len = len(sub_perm)
            if sub_perm_len <= 1:
                continue

            # check vehicles constraints
            customers_sum = 0
            for index in sub_perm:
                customers_sum += self.hmo_problem.customer_desires[index]
                customer_desire = self.hmo_problem.customer_desires[index]
                warehouses_constraints[warehouse_index] -= customer_desire
            if customers_sum > self.hmo_problem.vehicle_capacity:
                return -sys.maxint

            for i in range(sub_perm_len):
                if i + 1 == sub_perm_len:
                    break
                first = sub_perm[i]
                second = sub_perm[i + 1]
                cost += self.hmo_problem.ccdistances[first][second]

        for warehouse_index in used_warehouses:
            cost += self.hmo_problem.warehouse_prices[warehouse_index]

        return cost

if __name__ == '__main__':

    print 'CVRP evaluation module'
    solution = Solution({'int': [4, 0, 0, 0, 3, 0, 4, 0, 0, 0, 3, 0, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 4, 4, 0, 0, 0, 4, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0, 1, 1, 0, 0, 0, 0, 4, 4, 0, 0, 0, 4], 'permutation': [92, 25, 15, 69, 47, 78, 79, 34, 63, 66, 53, 76, 4, 36, 65, 98, 61, 5, 82, 46, 84, 90, 83, 39, 94, 30, 12, 22, 64, 81, 14, 73, 18, 93, 95, 62, 77, 88, 8, 86, 87, 74, 60, 17, 32, 20, 70, 23, 49, 42, 67, 58, 71, 31, 48, 35, 56, 27, 85, 96, 40, 0, 13, 52, 97, 9, 72, 19, 45, 57, 28, 51, 3, 7, 11, 26, 75, 38, 50, 1, 29, 54, 68, 33, 44, 99, 41, 21, 16, 43, 80, 91, 89, 6, 59, 55, 2, 37, 10, 24]})
    evaluator = Evaluator('input.txt')
    print evaluator.evaluate(solution)
