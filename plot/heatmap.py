# -*- coding: utf-8 -*-

'''
http://en.wikipedia.org/wiki/Heat_map
'''

import json
import numpy as np
from plot import Plot
import matplotlib.pyplot as plt
from helpers.setter import setter
from helpers.loader import load_json


def draw(plot, output_path=None):
    '''
    Plot a heatmap from the plot object.

    Args:
        plot:        instance of the Plot class

        output_path: path to output file, if the output_path is
                     None than graph will be shown inside a window

    '''

    # font setup
    plt.rc('font', family=plot.font_family)

    # get drawing space
    fig, ax = plt.subplots()

    # plot heatmaps and data
    heatmap = ax.pcolor(plot.data)
    for y in range(plot.data.shape[0]):
        for x in range(plot.data.shape[1]):
            plt.text(x + 0.5, y + 0.5, '%.2f' % plot.data[y, x],
                     horizontalalignment='center',
                     verticalalignment='center')

    # legend
    plt.colorbar(heatmap)

    # axis data setup
    ax.xaxis.tick_top()
    ax.yaxis.tick_left()
    ax.set_xticklabels(plot.xlabels, minor=False, fontsize=plot.font_size)
    ax.set_yticklabels(plot.ylabels, minor=False, fontsize=plot.font_size)
    ax.set_xticks(np.arange(0, len(plot.xlabels)) + 0.5)
    ax.set_yticks(np.arange(0, len(plot.ylabels)) + 0.5)

    # standard axis elements
    plt.xlabel(plot.yname, fontsize=plot.font_size)
    plt.ylabel(plot.xname, fontsize=plot.font_size)
    ax.yaxis.set_label_position("right")

    if output_path is None:
        plt.show()
    else:
        plt.savefig(output_path)


def plot_from_file(input_path, output_path=None):
    '''
    Plot a heatmap from the input file.

    Args:
        input_path:  path to input file which is in json format

        output_path: path to output file, if the output_path is
                     None than graph will be shown inside a window
    '''
    # load data from file
    plot_file = load_json(input_path)
    plot = Plot()
    plot.data = np.array(json.loads(plot_file.data))
    plot.yname = plot_file.yname
    plot.xname = plot_file.xname
    plot.ylabels = list(plot_file.ylabels)
    plot.xlabels = list(plot_file.xlabels)
    plot.font_size = setter(lambda: plot_file.font_size, 12)
    plot.font_family = setter(lambda: plot_file.font_family, 'serif')

    # draw plot
    draw(plot, output_path)
