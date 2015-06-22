# -*- coding: utf-8 -*-

'''
Multiple lines plot with log scale on the y-axis.
'''

from plot import Plot
from matplotlib import pyplot


def draw(plot, output_path=None):
    '''
    Mulitple lines plot.

    Args:
        plot: instance of Plot class
        output_path: output file path, if output_path is None
                     graph will be shown in a window
    '''
    lw = 2
    pyplot.rc('font', family=plot.font_family)
    pyplot.xlabel(plot.xname)
    pyplot.ylabel(plot.yname)
    pyplot.ylim([0, 400])

    # draw lines
    for label in plot.data.keys():
        xy = plot.data[label]
        xy = map(lambda x: tuple(x), xy)
        xy = zip(*xy)
        x, y = list(xy[0]), list(xy[1])
        pyplot.plot(x, y, lw=lw, label=label)
    legend = pyplot.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))

    # save of show plot
    if output_path is None:
        pyplot.show()
    else:
        pyplot.savefig(output_path, bbox_extra_artists=(legend,),
                       bbox_inches='tight')


def plot_from_file(input_path, output_path=None):
    '''
    Multiple lines plot.

    Args:
        inptu_path: path to the json input file
        outptu_path: output file path, if output_path is None
                     graph will be shown in a window
    '''
    plot, input_file = Plot().configure_file(input_path)
    plot.xname = input_file.xname
    plot.yname = input_file.yname
    plot.data = input_file.data
    draw(plot, output_path)
