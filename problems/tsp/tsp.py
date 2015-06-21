#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Definition of TSP instance.

Properties:
    distances -> 2D array of distances
    coords    -> array of coords
'''


class TSP(object):

    def __init__(self):
        self.distances = None
        self.coords = None
