#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class Tournament(object):
    '''
    '''
    def __init__(self, k=3):
        '''
        '''
        self.k = k

    def select(self, evaluations):
        '''
            evaluations is list of touples
            each touple contains index of genotype inside population and fitness
            for that genotype

            this is 3 tournament selection which choose 2 genotypes from the
            evaluations list for crossover
        '''

        size = len(evaluations)

        randoms = random.sample(xrange(size), self.k)

        selected = [evaluations[i] for i in randoms]

        selected = sorted(selected, key=lambda x: x[1], reverse=True)

        return (selected[0], selected[1])


if __name__ == '__main__':

    # test of tournament selection
    evaluations = [(0, 100), (1, 200), (3, 150), (4, 500), (5, 600)]

    print evaluations
    tournament = Tournament()
    print tournament.select(evaluations)
