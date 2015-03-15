#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import logging

log = logging.getLogger(__name__)


class DictWrapper(object):

    def __init__(self, input_dict):
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


def load_json(path):
    if os.path.isfile(path):
        with open(path) as f:
            return DictWrapper(json.load(f))
    else:
        return DictWrapper({})
