#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TSPLib problem loader
'''

import sys
import numpy as np
from tsp import TSP
from math import sqrt, pi as PI, cos, acos


class TSPLibLoader(object):

    def load(self, path):
        '''
        '''
        problem = TSP()
        data = extract_data(path)
        problem.distances = distances(data)
        return problem


# helpers start -----------------------------------------------------
def nint(number):
    return int(round(number))
# helpers end -------------------------------------------------------


# distance functions start ------------------------------------------
def euc_l2(coords):
    '''
    Euclidean distance (L2).

    Arguments:
        coords: array of coordinates

    Returns:
        Euclidean distance L2, integer value

    NOTE:
    Only 2D for now.
    '''
    c1, c2 = coords[0], coords[1]
    xd = c1[0] - c2[0]
    yd = c1[1] - c2[1]
    return nint(sqrt(xd ** 2 + yd ** 2))


def latlong(coord):
    '''
    Convert coord to (latitude, longitude)
    '''
    deg = nint(coord[0])
    _min = coord[0] - deg
    latitude = PI * (deg + 5.0 * _min / 3.0) / 180.0
    deg = nint(coord[1])
    _min = coord[1] - deg
    longitude = PI * (deg + 5.0 * _min / 3.0) / 180.0
    return (latitude, longitude)


def geo(coords):
    '''
    Distance from GEO coords.
    '''
    latitude_i, longitude_i = latlong(coords[0])
    latitude_j, longitude_j = latlong(coords[1])
    RRR = 6378.388
    q1 = cos(longitude_i - longitude_j)
    q2 = cos(latitude_i - latitude_j)
    q3 = cos(latitude_i + latitude_j)
    d = (int)(RRR * acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1)*q3)) + 1.0)
    return d


def att(coords):
    '''
    Pseudo-Euclidean distance.
    '''
    c1, c2 = coords[0], coords[1]
    xd = c1[0] - c2[0]
    yd = c1[1] - c2[1]
    rij = sqrt((xd ** 2 + yd ** 2) / 10.0)
    tij = nint(rij)
    if tij < rij:
        dij = tij + 1
    else:
        dij = tij
    return dij

distance_functions = {'ATT': att, 'EUC_2D': euc_l2, 'GEO': geo}
# distance functions end ----------------------------------------------------


# keys, types start -----------------------------------------------------------
EOF = 'EOF'
KV_SEPARATOR = ':'  # key value separator
EWT = 'EDGE_WEIGHT_TYPE'
EWF = 'EDGE_WEIGHT_FORMAT'
EWS = 'EDGE_WEIGHT_SECTION'
NCS = 'NODE_COORD_SECTION'
EXPLICIT = 'EXPLICIT'
DIMENSION = 'DIMENSION'
FULL_MATRIX = 'FULL_MATRIX'
UPPER_ROW = 'UPPER_ROW'
# keys, types end -------------------------------------------------------------


def extract_data(path):
    '''
    Load file to the data dict.

    Args:
        path: file path

    Returns:
        data dictionary
    '''
    data = {}
    buffer_key = None
    buffer_value = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == EOF:
                data[buffer_key] = buffer_value
                break
            if KV_SEPARATOR in line:
                keyvalue = line.split(KV_SEPARATOR)
                key = keyvalue[0].strip()
                value = keyvalue[1].strip()
                data[key] = value
                continue
            if line and line[0].isalpha():
                if buffer_key is not None:
                    data[buffer_key] = buffer_value
                buffer_key = line
                buffer_value = []
            else:
                buffer_value.append([e.strip() for e in line.split()])
    return data


def distances(data):
    '''
    '''
    if data[EWT] == EXPLICIT:
        return explicit(data)
    else:
        return function(data)


# explicit edge weight type start ---------------------------------------------
def explicit(data):
    return explicit_matrix[data[EWF]](data)


def full_matrix(data):
    dim = int(data[DIMENSION])
    dist = np.zeros((dim, dim))
    for row in xrange(dim):
        for col in xrange(dim):
            if row == col:
                continue
            else:
                dist[row][col] = float(data[EWS][row][col])
    return dist


def upper_row(data):
    dim = int(data[DIMENSION])
    dist = np.zeros((dim, dim))
    for row in xrange(dim):
        for col in xrange(dim):
            if row == col:
                continue
            if col > row:
                dist[row][col] = float(data[EWS][row][col - row - 1])
                dist[col][row] = dist[row][col]
            else:
                dist[row][col] = float(data[EWS][col][row - col - 1])
                dist[col][row] = dist[row][col]
    return dist


explicit_matrix = {FULL_MATRIX: full_matrix, UPPER_ROW: upper_row}
# explicti edge weight type end -----------------------------------------------


# function edge type start ----------------------------------------------------
def function(data):
    '''
    '''
    dim = int(data[DIMENSION])
    dist = np.zeros((dim, dim))
    function_type = data[EWT]
    distance_function = distance_functions[function_type]
    coords = [(float(x[1]), float(x[2])) for x in data[NCS]]
    for row in xrange(dim):
        for col in xrange(dim):
            if row == col:
                continue
            else:
                dist[row][col] = distance_function((coords[row], coords[col]))
    return dist
# function edge type end ------------------------------------------------------


if __name__ == '__main__':

    print 'tsp lib loader'

    path = sys.argv[1]
    loader = TSPLibLoader()
    tsp = loader.load(path)
    print tsp.distances
