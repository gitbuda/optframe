#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Population(object):

    def __init__(self):
        self._genotypes = []

    @property
    def genotypes(self):
        return self._genotypes

    @genotypes.setter
    def genotypes(self, value):
        self._genotypes = self

    @property
    def size(self):
        return len(self._genotypes)

    def append(self, genotype):
        self._genotypes.append(genotype)

    def put(self, genotype, to_index):
        self._genotypes[to_index] = genotype
