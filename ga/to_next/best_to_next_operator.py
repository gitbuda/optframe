#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BestToNextOperator(object):

    def __init__(self, how_many):
        self._how_many = how_many

    def to_next(self, evaluations):

        sorted_evaluatins = sorted(evaluations,
                                   key=lambda x: x[1],
                                   reverse=True)

        return sorted_evaluatins[0:self._how_many]


if __name__ == '__main__':

    # test of tournament selection
    evaluations = [(0, 100), (1, 200), (3, 150), (4, 500), (5, 600)]

    operator = BestToNextOperator(3)

    print operator.best(evaluations)
