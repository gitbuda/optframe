#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
optframe (initial script)
'''

import time
import logging
import common.constants as CONF

from helpers.arguments import get_arg
from helpers.dict_wrapper import load_json
from helpers.load_package import load_package
from helpers.path import unique_path


if __name__ == '__main__':

    # logger setup
    logging.basicConfig(level=logging.DEBUG)
    handler = logging.FileHandler(unique_path('output', 'log'))
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s  %(message)s')
    handler.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(handler)

    # load modules (algorithms and problems)
    problems = load_package(CONF.PROBLEMS_DIRNAME, 'Problem')
    algorithms = load_package(CONF.ALGORITHMS_DIRNAME, 'Algorithm')
    executors = load_package(CONF.EXECUTORS_DIRNAME, 'Executor')

    # load config
    config_file_name = get_arg('-c', CONF.CONFIG_FILE_NAME)
    execution_context = load_json(config_file_name)

    # execution delay
    # TODO: remove this from here
    time.sleep(1)

    for executor_name in execution_context.keys():
        executor = executors[executor_name].executor
        config = execution_context[executor_name]
        executor.execute(algorithms, problems, config)
