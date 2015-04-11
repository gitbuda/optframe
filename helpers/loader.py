#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import logging

log = logging.getLogger(__name__)


class DictWrapper(object):

    def __init__(self, input_dict={}):
        self._input_dict = input_dict

    @property
    def input_dict(self):
        return self._input_dict

    def __getattr__(self, key):
        value = self.input_dict[key]
        if type(value) is dict:
            return DictWrapper(value)
        elif type(value) is list:
            return [item if type(item) is not dict else
                    DictWrapper(item) for i, item in enumerate(value)]
        else:
            return value

    def __contains__(self, key):
        # TODO: recursive implementation
        if key in self.input_dict:
            return True
        else:
            return False

    def weak_set(self, name, value):
        if name not in self.input_dict:
            self.hard_set(name, value)

    def hard_set(self, name, value):
        self.input_dict[name] = value

    def weak_merge(self, merge_dict):
        # TODO: recursive implementation
        for key, value in merge_dict.input_dict.items():
            self.weak_set(key, value)

    def hard_merge(self, merge_dict):
        # TODO: recursive implementation
        for key, value in merge_dict.input_dict.items():
            self.hard_set(key, value)

    def __str__(self):
        # TODO: recursive implementation
        representation = ''
        for key, value in self.input_dict.items():
            representation += '%s: %s\n' % (key, value)
        return representation


def load_json(path):
    if os.path.isfile(path):
        with open(path) as f:
            return DictWrapper(json.load(f))
    else:
        return DictWrapper()
