#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import math
import random
import logging

from common.solution import Solution
from common.constants import BIT_BOX_KEY

log = logging.getLogger(__name__)
fact = math.factorial


class GraphNode(object):
    '''
    parents -> list of parent nodes (only indices)
    childs -> list of child nodes (only indices)
    '''
    def __init__(self, index):
        '''
        '''
        self.index = index
        self.parents = []
        self.childs = []

    def __str__(self):
        '''
        '''
        return "Childs: %s, Parents: %s, Index: %s" % \
            (self.childs, self.parents, self.index)


def random_bitstr(length):
    '''
    random bit string
    '''
    return [random.randint(0, 1) for x in xrange(length)]


def path_exists(i, j, graph):
    '''
    BFS to determine path existance
    i - start node index
    j - end node index
    graph - list of nodes
    '''
    visited, stack = [], [i]
    while stack:
        if j in stack:
            return True
        k = stack.pop(0)
        if k in visited:
            continue
        visited.append(k)
        for child in graph[k].childs:
            if child not in visited:
                stack.insert(0, child)
    return False


def can_add_edge(i, j, graph):
    '''
    edge can't be added if the same edge already exists
    and if edge from i to j will make cycle
    '''
    return (j not in graph[i].childs) and (not path_exists(j, i, graph))


def get_viable_parents(node, graph):
    '''
    returns list of parent candidates
    '''
    viable = []
    for i in xrange(len(graph)):
        if (node is not i) and can_add_edge(node, i, graph):
            viable.append(i)
    return viable


def compute_count_for_edges(population, indexes):
    '''
    '''
    # print indexes
    counts = [0 for x in xrange(2 ** len(indexes))]
    for solution in population:
        index = 0
        for i, v in enumerate(reversed(indexes)):
            index += (solution.container[BIT_BOX_KEY][v] * (2 ** i))
        counts[index] += 1
    return counts


def k2equation(node, candidates, population):
    '''
    '''
    counts = compute_count_for_edges(population, [node] + candidates)
    total = 1.0
    for i in xrange(len(counts) / 2):
        a1, a2 = counts[i*2], counts[(i*2) + 1]
        rs = (1.0 / float(fact(a1 + a2 + 1)))*float(fact(a1))*float(fact(a2))
        total *= rs
    return total


def compute_gains(node, graph, population, max_parents=2):
    '''
    '''
    viable = get_viable_parents(node.index, graph)
    gains = [-1 for x in xrange(len(graph))]
    for i in xrange(len(gains)):
        if (len(graph[i].parents) < max_parents) and (i in viable):
            gains[i] = k2equation(node.index, node.parents + [i], population)
    return gains


def construct_network(population, solution_size, max_edges):
    '''
    '''
    graph = [GraphNode(index) for index in xrange(solution_size)]
    for iteration in xrange(max_edges):
        max_v, from_n, to_n = -1, None, None
        for i, node in enumerate(graph):
            gains = compute_gains(node, graph, population)
            for j, v in enumerate(gains):
                if v > max_v:
                    from_n, to_n, max_v = i, j, v
        if max_v <= 0.0:
            break
        graph[from_n].childs.append(to_n)
        graph[to_n].parents.append(from_n)
    return graph


def topological_ordering(graph):
    '''
    '''
    for node in graph:
        node.count = len(node.parents)
    ordered, stack = [], [node for node in graph if node.count == 0]
    while len(ordered) < len(graph):
        current = stack.pop(0)
        for edge in current.childs:
            node = graph[edge]
            node.count -= 1
            if node.count <= 0:
                stack.append(node)
        ordered.append(current)
    # generate_directed(graph, "// ordered: %s\n" %
    #                   str(map(lambda x: x.index, ordered)))
    return ordered


def margin_probability(i, population):
    '''
    '''
    prob = 1.0 * sum(map(lambda x: x.container[BIT_BOX_KEY][i], population)) /\
        len(population)
    return prob


def calculate_probability(node, bitstr, population):
    '''
    '''
    # print node.index, node.parents
    if len(node.parents) == 0:
        return margin_probability(node.index, population)
    counts = compute_count_for_edges(population, [node.index] + node.parents)
    index = 0
    for i, v in enumerate(reversed(node.parents)):
        index += (bitstr[v] * (2**i))
    i1 = index + (1*2**len(node.parents))
    i2 = index + (0*2**len(node.parents))
    a1, a2 = float(counts[i1]), float(counts[i2])
    try:
        rez = a1 / (a1 + a2)
        return rez
    except:
        return 0


def sample(graph, population):
    '''
    Probabilistic Logic sample
    '''
    bitstr = [0 for x in xrange(len(graph))]
    for node in graph:
        prob = calculate_probability(node, bitstr, population)
        bitstr[node.index] = 1 if random.random() < prob else 0
    return Solution({BIT_BOX_KEY: bitstr}, None)


def sample_from_network(population, graph, children_number):
    '''
    '''
    ordered = topological_ordering(graph)
    return [sample(ordered, population) for x in xrange(children_number)]


if __name__ == '__main__':
    pass
