# Description: Utility functions for the application
import json
from datetime import datetime
import datetime
import re

import requests
import urllib3


# Read local json file
def read_json_local(path: str) -> list:
    """
    Read a local json file
    :param path: string path to the file
    :return: list[Dictionaries]
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# Read json from a URL
def read_json_url(url: str) -> list:
    """
    Read a json file from a URL
    :param url: string URL to the file
    :return: list[Dictionaries]
    """
    urllib3.disable_warnings()
    data = requests.get(url, verify=False).json()
    return data


# Filter data by key
def filter_data(data: list, key: str, value: str) -> list:
    """
    Filter data by key
    :param data: list of dictionaries
    :param key: key of the dictionary
    :param value: value of the key
    :return: new filtered list
    """
    new_data = [i for i in data if i.get(key) == value]
    return new_data


# Sort data by key
def sort_data(data, key, reverse=False, limit=None):
    """
    Sort data by key
    :param data:
    :param key:
    :param reverse:
    :param limit:
    :return:
    """
    new_data = sorted(data, key=lambda x: x.get(key), reverse=reverse)
    if limit:
        new_data = new_data[:limit]
    return new_data


# Convert date to needs format
def convert_date(date: str, format_to="%d.%m.%Y") -> datetime:
    """
    Convert date to needs format
    :param format_to:
    :param date: string date
    :return: string date
    """
    return datetime.datetime.fromisoformat(date).strftime(format_to)


# Split type and number
def split_type_number(string: str) -> dict:
    """
    Split type and number
    :param string:
    :return:
    """
    pattern = r"(\D+) (\d+)"
    match = re.search(pattern, string)
    if match:
        type_ = match.group(1).strip()
        number_ = match.group(2).strip()
        return {'type': type_, 'number': number_}
    # return {}


# Set private string
def set_private_string(string: str, area_start: int, area_end: int) -> str:
    """
    Set private string
    :param string:
    :param area_start:
    :param area_end:
    :return:
    """
    private_area = string[area_start:area_end]
    return string.replace(private_area, '*' * len(private_area))

# ru: разбиение строки на группы по n символов
# en: split string into groups of n characters


def regroup_string(string: str, n: int) -> str:
    """
    regroup string into groups of n characters
    :param string:
    :param n:
    :return:
    """
    return ' '.join([string[i:i + n] for i in range(0, len(string), n)])
