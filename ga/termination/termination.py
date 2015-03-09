#!/usr/bin/env python
# -*- coding: utf-8 -*-


def max_iteration(max_iteration_no):
    current = 1
    while current <= max_iteration_no:
        yield current
        current += 1
