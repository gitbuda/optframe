#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import os
import random
import logging
import lxml.etree as etree
from common.solution import Solution
import common.constants as CONST

log = logging.getLogger(__name__)


class Individual(object):
    def __init__(self, fitness, genotype):
        self.fitness = fitness
        self.genotype = genotype


def deme_reader(path='deme.txt'):
    tree = etree.parse(path)
    root = tree.getroot()
    deme = []
    for child in root.findall('Individual'):
            fitness = float(child.find('FitnessMin').get('value'))
            genotype = map(int, list(child.find('BitString').text))
            deme.append(Individual(fitness, genotype))
    return deme


class SolutionOperator(object):

    def __init__(self):
        folder_path = os.path.split(os.path.abspath(__file__))[0]
        deme_path = os.path.join(folder_path, 'deme.txt')
        self.deme = deme_reader(deme_path)

    def next(self):
        index = random.randint(0, len(self.deme) - 1)
        genotype = self.deme[index].genotype
        container = {}
        container[CONST.BIT_BOX_KEY] = genotype
        return Solution(container)


if __name__ == '__main__':

    folder_path = os.path.split(os.path.abspath(__file__))[0]
    deme_path = os.path.join(folder_path, 'deme.txt')

    deme = deme_reader(deme_path)

    for individual in deme:
        print individual.fitness
        print individual.genotype
