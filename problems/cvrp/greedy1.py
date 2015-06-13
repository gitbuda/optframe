#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from common.solution import Solution
from problems.cvrp.hmo_loader import read_hmo_file


def give_warehouse(clusters, customer, hmo_problem, curr_wcap):
    for i, w in enumerate(clusters[customer][2]):
        w_index = w[0] - 1
        if curr_wcap[w_index] - hmo_problem.customer_desires[customer] < 0:
            continue
        return w_index


class Greedy(object):

    def configure(self, config):
        '''
        '''
        self.hmo_problem = read_hmo_file(config.path)
        self.warehouses = config.warehouses
        return self

    def run(self):

        hmo_problem = self.hmo_problem
        warehouses = self.warehouses

        CLUSTERS_NO = hmo_problem.customers_no
        NEIGHBOORS_NO = hmo_problem.customers_no
        WAREHOUSES_NO = len(warehouses)
        CUSTOMERS_NO = hmo_problem.customers_no

        centroids = [i for i in range(CLUSTERS_NO)]

        clusters = []

        for i, centroid in enumerate(centroids):

            cdistances = []
            for j in range(CUSTOMERS_NO):
                cdistances.append((j, hmo_problem.ccdistances[centroid][j]))
            cdistances = sorted(cdistances, key=lambda x: x[1])

            wdistances = []
            for j, w in enumerate(warehouses):
                wdistances.append((w, hmo_problem.wcdistances[w][centroid]))
            wdistances = sorted(wdistances, key=lambda x: x[1])

            clusters.append((centroid,
                             cdistances[1:NEIGHBOORS_NO + 1],
                             wdistances[0:WAREHOUSES_NO]))

        vehicle_capacity = hmo_problem.vehicle_capacity
        warehouse_capacities = list(hmo_problem.warehouse_capacities)

        customers = [i for i in range(CUSTOMERS_NO)]
        random.shuffle(customers)

        chosen = set()
        visits = []
        for i, customer in enumerate(customers):
            if customer in chosen:
                continue
            chosen.add(customer)
            from_warehouse = give_warehouse(clusters, customer, hmo_problem,
                                            warehouse_capacities)
            warehouse_capacities[from_warehouse] -= \
                hmo_problem.customer_desires[customer]
            visited_customers = []
            visited_customers.append(customer)
            curr_vehicle_cap = vehicle_capacity - \
                hmo_problem.customer_desires[customer]
            for j, neigh in enumerate(clusters[customer][1]):
                curr_neigh = neigh[0]
                if curr_neigh in chosen:
                    continue
                neigh_desires = hmo_problem.customer_desires[curr_neigh]
                if curr_vehicle_cap - neigh_desires < 0:
                    break
                if warehouse_capacities[from_warehouse] - neigh_desires < 0:
                    break
                desire = hmo_problem.customer_desires[curr_neigh]
                curr_vehicle_cap -= desire
                warehouse_capacities[from_warehouse] -= desire
                chosen.add(curr_neigh)
                visited_customers.append(curr_neigh)
            visits.append((from_warehouse + 1, visited_customers))

        output_list_head = []
        output_list_tail = []
        for i, group in enumerate(visits):
            warehouse = group[0]
            customers = group[1]
            output_list_head += [warehouse] + \
                [0 for i in range(len(customers) - 1)]
            output_list_tail += customers

        container = {'int': output_list_head, 'permutation': output_list_tail}

        return Solution(container)


if __name__ == '__main__':

    from problems.cvrp.hmo_output import write
    from helpers.dict_wrapper import DictWrapper
    from problems.cvrp.evaluator import Evaluator

    print 'CVRP manual test'

    config = DictWrapper({'path': 'input.txt', 'warehouses': [2, 4, 5]})
    greedy = Greedy().configure(config)
    solution = greedy.run()
    evaluator = Evaluator().configure(config)
    fitness = evaluator.evaluate(solution)
    solution.fitness = fitness
    write('example.txt', solution)
    print solution
