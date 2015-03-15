#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Genotype(object):

    def __init__(self, genes=[]):
        self._genes = genes

    @property
    def size(self):
        return len(self._genes)

    @property
    def genes(self):
        return self._genes

    @genes.setter
    def genes(self, value):
        self._genes = value
