#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random
from common.solution import Solution
from problems.cvrp.hmo_loader import read_hmo_file


# https://en.wikipedia.org/wiki/Cumulative_distribution_function
def roulette_wheel(weights):
    r = random.random()
    index = 0
    while(r >= 0 and index < len(weights)):
        r -= weights[index]
        index += 1
    return index - 1


class WarehouseSource(object):

    def __init__(self, cvrp):
        self.cvrp = cvrp

    def reset(self):
        self.chosen = set()

    def next(self, forbidden):
        k = int(math.pow(2, len(self.chosen)) * self.cvrp.warehouses_no)
        multiplier = lambda (i, x): x * k if i in self.chosen else x
        filter_lambda = lambda (i, x): 0 if i in forbidden else x
        weights = map(multiplier, enumerate(self.cvrp.warehouse_prices))
        filtered = map(filter_lambda, enumerate(weights))
        sum_filtered = sum(filtered)
        normalized = [float(x) / sum_filtered for x in filtered]
        index = roulette_wheel(normalized)
        self.chosen.add(index)
        return index


class Greedy(object):

    def configure(self, config):
        '''
        '''
        self.hmo_problem = read_hmo_file(config.path)
        self.ws = WarehouseSource(self.hmo_problem)

        wcdistances = self.hmo_problem.wcdistances
        ccdistances = self.hmo_problem.ccdistances

        # TODO: ugly, requires numpy rewrite
        self.wc_sorted = []
        for w in xrange(self.hmo_problem.warehouses_no):
            self.wc_sorted.append([])
            for c in xrange(self.hmo_problem.customers_no):
                self.wc_sorted[w].append((c, wcdistances[w][c]))
            self.wc_sorted[w] = sorted(self.wc_sorted[w], key=lambda x: x[1])

        self.cc_sorted = []
        for c1 in xrange(self.hmo_problem.customers_no):
            self.cc_sorted.append([])
            for c2 in xrange(self.hmo_problem.customers_no):
                self.cc_sorted[c1].append((c2, ccdistances[c1][c2]))
            self.cc_sorted[c1] = sorted(self.cc_sorted[c1], key=lambda x: x[1])

        return self

    def random_customer(self, pool, used):
        squares = map(lambda (c, d): 1.0 / d**5 if c not in used else 0, pool)
        sumall = sum(squares)
        probs = map(lambda x: x / sumall, squares)
        index = roulette_wheel(probs)
        return pool[index][0]

    def run(self):
        '''
        '''
        self.ws.reset()
        self.emptiness_wh = {}
        # chosen warehouses
        self.forbidden_wh = set()
        # chosen customers
        self.chosen_c = set()
        solution = []
        w_capacities = self.hmo_problem.warehouse_capacities

        while len(self.chosen_c) != self.hmo_problem.customers_no:
            wh = self.ws.next(self.forbidden_wh)
            if wh not in self.emptiness_wh:
                self.emptiness_wh[wh] = int(w_capacities[wh])
            capacity = int(self.hmo_problem.vehicle_capacity)
            customers = []
            while True:
                if len(self.chosen_c) == self.hmo_problem.customers_no:
                    break
                customer = self.random_customer(self.wc_sorted[wh],
                                                self.chosen_c)
                desire = self.hmo_problem.customer_desires[customer]
                capacity -= desire
                self.emptiness_wh[wh] -= desire
                if capacity < 0:
                    if self.emptiness_wh[wh] < 0:
                        self.forbidden_wh.add(wh)
                    break
                if self.emptiness_wh[wh] < 0:
                    self.forbidden_wh.add(wh)
                    break
                if customer in self.chosen_c:
                    break
                else:
                    customers.append(customer)
                    self.chosen_c.add(customer)
            if len(customers) > 0:
                solution.append((wh, customers))

        int_box = []
        perm_box = []
        for warehouse, customers in solution:
            int_box += [warehouse + 1] + [0] * (len(customers) - 1)
            perm_box += customers

        return Solution({'int': int_box, 'permutation': perm_box})


if __name__ == '__main__':

    from problems.cvrp.hmo_output import write
    from helpers.dict_wrapper import DictWrapper
    from problems.cvrp.evaluator import Evaluator

    print 'CVRP greedy2 manual test'

    config = DictWrapper({'path': 'input.txt'})
    greedy = Greedy().configure(config)
    solution = greedy.run()
    evaluator = Evaluator().configure(config)
    fitness = evaluator.evaluate(solution)
    solution.fitness = fitness
    write('output/greedy2.txt', solution)
    print solution
