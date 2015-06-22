#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
matplotlib router

the script plots graph written in python
'''

from helpers.arguments import get_arg
from heatmap import plot_from_file as heatmap
from radar import plot_from_file as radar
from linelogy import plot_from_file as linelogy
from multiline import plot_from_file as multiline

graphs = {}
graphs['heatmap'] = heatmap
graphs['radar'] = radar
graphs['linelogy'] = linelogy
graphs['multiline'] = multiline

if __name__ == '__main__':

    graph_type = get_arg('-t', None)
    input_path = get_arg('-i', None)
    output_path = get_arg('-o', None)

    if graph_type is not None and input_path is not None:
        graphs[graph_type](input_path, output_path)
