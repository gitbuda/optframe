#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Standard dictionary wrapper.

The main reason of existance of this class
is the possibility to access to the elements
of some dictionary via dot notation.
'''

import os
import json


class DictWrapper(object):

    def __init__(self, input_dict={}):
        self.input_dict = input_dict

    def keys(self):
        return self.input_dict.keys()

    def __getitem__(self, key):
        return self.__getattr__(key)

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
        for key, value in merge_dict.input_dict.items():
            self.weak_set(key, value)

    def hard_merge(self, merge_dict):
        for key, value in merge_dict.input_dict.items():
            self.hard_set(key, value)

    def __str__(self):
        representation = ''
        for key, value in self.input_dict.items():
            representation += '%s: %s\n' % (key, value)
        return representation[:-1]

    def store(self, path):
        with open(path, 'wb') as f:
            json.dump(self.input_dict, f)


def load_json(path):
    if os.path.isfile(path):
        with open(path) as f:
            return DictWrapper(json.load(f))
    else:
        return DictWrapper({})


if __name__ == '__main__':
    wrapper = DictWrapper()
    print wrapper
