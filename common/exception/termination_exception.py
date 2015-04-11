#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Somebody will raise TerminationException if
it goes into a termination state.

e.g.
If best fitness value constraint is reached then an
algorithm has to expect this type of exception.
'''


class TerminationException(Exception):
    pass
