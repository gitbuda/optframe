#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class HMOProblem(object):

    def __init__(self):
        self._warehouses_no = 0
        self._customers_no = 0
        self._warehouses_coords = []
        self._customers_coords = []
        self._vehicle_capacity = 0
        self._warehouse_capacities = []
        self._customer_desires = []
        self._warehouse_prices = []
        self._vehicle_price = 0
        self._ccdistances = defaultdict(lambda: defaultdict(list))
        self._wcdistances = defaultdict(lambda: defaultdict(list))

    @property
    def warehouses_no(self):
        return self._warehouses_no

    @warehouses_no.setter
    def warehouses_no(self, value):
        self._warehouses_no = value

    @property
    def customers_no(self):
        return self._customers_no

    @customers_no.setter
    def customers_no(self, value):
        self._customers_no = value

    @property
    def warehouses_coords(self):
        return self._warehouses_coords

    @warehouses_coords.setter
    def warehouses_coords(self, value):
        self._warehouses_coords = value

    @property
    def customers_coords(self):
        return self._customers_coords

    @customers_coords.setter
    def customers_coords(self, value):
        self._customers_coords = value

    @property
    def vehicle_capacity(self):
        return self._vehicle_capacity

    @vehicle_capacity.setter
    def vehicle_capacity(self, value):
        self._vehicle_capacity = value

    @property
    def warehouse_capacities(self):
        return self._warehouse_capacities

    @warehouse_capacities.setter
    def warehouse_capacities(self, value):
        self._warehouse_capacities = value

    @property
    def customer_desires(self):
        return self._customer_desires

    @customer_desires.setter
    def customer_desires(self, value):
        self._customer_desires = value

    @property
    def warehouse_prices(self):
        return self._warehouse_prices

    @warehouse_prices.setter
    def warehouse_prices(self, value):
        self._warehouse_prices = value

    @property
    def vehicle_price(self):
        return self._vehicle_price

    @vehicle_price.setter
    def vehicle_price(self, value):
        self._vehicle_price = value

    @property
    def ccdistances(self):
        return self._ccdistances

    @property
    def wcdistances(self):
        return self._wcdistances

    def distance(self, a, b):
        return int(pow(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2), 0.5) * 100)

    def calculate_distances(self):
        for i in range(self.customers_no):
            for j in range(self.customers_no):
                first_coords = self.customers_coords[i]
                second_coords = self.customers_coords[j]
                distance = self.distance(first_coords, second_coords)
                self.ccdistances[i][j] = distance
        for i in range(self.warehouses_no):
            for j in range(self.customers_no):
                first_coords = self.warehouses_coords[i]
                second_coords = self.customers_coords[j]
                distance = self.distance(first_coords, second_coords)
                self.wcdistances[i][j] = distance


def read_coords(f, lines_no):
    data_array = []
    for i in range(lines_no):
        string_list = f.readline().rstrip('\r\n').split('\t')
        data_array.append(tuple(int(num) for num in string_list))
    return data_array


def read_values(f, lines_no):
    data_array = []
    for i in range(lines_no):
        capacity_string = f.readline().rstrip('\r\n')
        data_array.append(int(capacity_string))
    return data_array


def read_hmo_file(path):
    hp = HMOProblem()
    with open(path) as f:
        hp.customers_no = int(f.readline().rstrip('\r\n'))
        hp.warehouses_no = int(f.readline().rstrip('\r\n'))
        f.readline()
        hp.warehouses_coords = read_coords(f, hp.warehouses_no)
        f.readline()
        hp.customers_coords = read_coords(f, hp.customers_no)
        f.readline()
        hp.vehicle_capacity = int(f.readline().rstrip('\r\n'))
        f.readline()
        hp.warehouse_capacities = read_values(f, hp.warehouses_no)
        f.readline()
        hp.customer_desires = read_values(f, hp.customers_no)
        f.readline()
        hp.warehouse_prices = read_values(f, hp.warehouses_no)
        f.readline()
        vehicle_price = f.readline().rstrip('\r\n')
        hp.vehicle_price = int(vehicle_price)
    hp.calculate_distances()
    return hp


if __name__ == '__main__':

    hmo_problem = read_hmo_file('input.txt')

    print hmo_problem.warehouses_no
    print hmo_problem.customers_no
    print hmo_problem.warehouses_coords  #
    print hmo_problem.customers_coords  #
    print 'vehicle capacity', hmo_problem.vehicle_capacity  #
    print hmo_problem.warehouse_capacities  #
    print hmo_problem.customer_desires  #
    print hmo_problem.warehouse_prices  #
    print hmo_problem.vehicle_price  #
    hmo_problem.calculate_distances()
    print hmo_problem.ccdistances[51][50]
    print hmo_problem.ccdistances[50][51]
    print hmo_problem.wcdistances[4][23]
