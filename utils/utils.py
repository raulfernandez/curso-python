#!/usr/bin/env python3
from json import dump, load
from requests import request

"""
    Utility module
"""


def load_json(file_name):
    obj = {}

    try:
        json_file = open(f'C:/git/curso-python/json/{file_name}', 'r')
        obj = load(json_file)
        json_file.close()
    except Exception as ex:
        print('Error', ex)

    return obj


def dump_json(file_name, obj):
    try:
        json_file = open(f'C:/git/curso-python/json/{file_name}', 'w')
        dump(obj, json_file)
        json_file.close()
    except Exception as ex:
        print('Error', ex)


def get(url: str) -> dict:
    data = request('GET', url)
    return data.json()


def post(url: str) -> dict:
    data = request('POST', url)
    return data.json()
