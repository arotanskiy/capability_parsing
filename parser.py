#!/usr/bin/env python3
"""
This for parsing LTE capabilities files
"""
import json
import os
import re
import logging


formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)
log = logging.getLogger('parser')
log.setLevel(logging.INFO)

def read_param_list():
    """
    This load json file with list of params what shall be parsed
    :param: capab_keys_list.json
    :return: list of names of parameters what will be parsed
    """
    log = logging.getLogger('parser.param_list')
    try:
        log.info('Loading capability params list file')
        with open('capab_keys_list.json', 'r') as file:
            params = file.read()
    except Exception:
        log.error('capab_keys_list.json with params shall be located in a current dir')
        log.error('program interrupted....................')
        exit(1)

    param_list: dict
    param_list = json.loads(params)

    # THIS IS AN EXAMPLE PRINT SECTION
    # this is for example and print params with value
    # uncomment block below to see printouts:

    # for key, value in param_list.items():
    #     log.info('key: %s  value: %s', key, value)
    # # this is for example and print only params
    # for key in param_list:
    #     log.info('Current parameter: {}'.format(key))
    # # this is for example and print only values of params
    # for value in param_list.values():
    #     log.info('Current type of parameter: %s', value)

    return param_list

def read_cap_file():
    """
        This search and load txt file what shall be parsed in current dir
        :param file: file.txt
        :return:
    """
    log = logging.getLogger('parser.cap_file')
    log.info('Loading device capability file')
    file_type = '.txt'
    file_cap_list = []
    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.endswith(file_type):
                file_cap_list.append(file)

    if len(file_cap_list) < 1:
        log.exception('No any device capability file has been found')
        log.error('program interrupted......................')
        exit(1)
    elif len(file_cap_list) > 1:
        log.error('More than one device capability file has been found, please leave only one')
        log.error('program interrupted......................')
        exit(1)
    else:
        log.info('%s device capability file will be parsed', file_cap_list[0])

    with open(file_cap_list[0], 'r') as file:
        caps = file.read().splitlines()

    return caps

def parse_capabilities():
    """
    This parse device capabilities file using capabilities parameter list
    :param param_list:
    :param caps:
    :return:
    """

    param_list = read_param_list()
    caps = read_cap_file()
    param_dict = []
    for param, value in param_list.items():
        line_count = 0
        num = 0
        for line in caps:
            if re.search(param, line):
                if isinstance(value, int):
                    num = line_count + value
            if line_count < num:
                param_dict.append(line)
            line_count += 1

    for param in param_dict:
        print(param)


parse_capabilities()