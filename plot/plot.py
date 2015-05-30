# -*- coding: utf-8 -*-

'''
Plot informations container.
'''

from helpers.setter import setter
from helpers.loader import load_json


class Plot(object):

    def configure_file(self, path):
        '''
        '''
        plot_file = load_json(path)
        self.font_size = setter(lambda: plot_file.font_size, 12)
        self.font_family = setter(lambda: plot_file.font_family, 'serif')
        return self, plot_file
