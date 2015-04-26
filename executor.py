#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
optframe (initial script)
'''

import logging
import common.constants as CONF

from helpers.arguments import get_arg
from helpers.loader import load_json
from helpers.load_package import load_package


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    # load modules (algorithms and problems)
    problems = load_package(CONF.PROBLEMS_DIRNAME, 'Problem')
    algorithms = load_package(CONF.ALGORITHMS_DIRNAME, 'Algorithm')
    executors = load_package(CONF.EXECUTORS_DIRNAME, 'Executor')

    # load config
    config_file_name = get_arg('-c', CONF.CONFIG_FILE_NAME)
    execution_context = load_json(config_file_name)

    for executor_name in execution_context.keys():
        executor = executors[executor_name].executor
        config = execution_context[executor_name]
        executor.execute(algorithms, problems, config)
