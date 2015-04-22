#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import logging

log = logging.getLogger(__name__)


def generate_directed(graph, header_text=''):

    path = 'output/directed.dot'

    parents_str = ("// parents: %s\n" %
                   str(map(lambda x: (x.index, x.parents), graph)))
    childs_str = ("// childs: %s\n" %
                  str(map(lambda x: (x.index, x.childs), graph)))
    graph_str = "%s%s%s" % (header_text, parents_str, childs_str)

    graph_str += "digraph directed {\n"

    for node in graph:
        for child in node.childs:
            graph_str += "\t%s -> %s;\n" % (node.index, child)

    graph_str += "}\n"

    with open(path, 'w') as f:
        f.write(graph_str)

if __name__ == '__main__':
    pass
