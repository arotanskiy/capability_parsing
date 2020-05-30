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
logger = logging.getLogger('parser')
logger.setLevel(logging.INFO)

def read_param_list():
    """
    This load json file with list of params what shall be parsed
    :param: capab_keys_list.json
    :return: list of names of parameters what will be parsed
    """
    logger = logging.getLogger('parser.param_list')
    try:
        logger.info('Loading capability params list file')
        with open('capab_keys_list.json', 'r') as file:
            params = file.read()
    except FileNotFoundError:
        logger.error('capab_keys_list.json with params shall be located in a current dir')
        logger.error('program interrupted....................')
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
    logger = logging.getLogger('parser.cap_file')
    logger.info('Loading device capability file')
    file_type = '.txt'
    file_cap_list = []
    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.endswith(file_type):
                file_cap_list.append(file)

    if len(file_cap_list) < 1:
        logger.exception('No any device capability file has been found')
        logger.error('program interrupted......................')
        exit(1)
    elif len(file_cap_list) > 1:
        logger.error('More than one device capability file has been found, please leave only one')
        logger.error('program interrupted......................')
        exit(1)
    else:
        logger.info('%s device capability file will be parsed', file_cap_list[0])

    with open(file_cap_list[0], 'r') as file:
        caps = file.read().splitlines()

    return caps

def parse_line(line):
    """
    This parse a simple string, separate and return two key and value
    :param line:
    :return:
    """
    pass

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
    start = end = 0
    line_count = 0
    for param, value in param_list.items():
        for line in caps:
            line_count += 1
            if isinstance(value, int):
                if re.search(param, line):
                    start = line_count + 1
                    end = line_count + value
                if start < line_count < end:
                    param_dict.append(line)

    # for i in param_dict:
    #     print(i)

# parse_capabilities()
line = "supportedBandwidthCombinationSet-r10 :  ---- '111'B ---- *****00010111***"
parse_line(line)
