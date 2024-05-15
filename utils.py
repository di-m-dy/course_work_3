# Description: Utility functions for the application
import json
import requests


# Read local json file
def read_json_local(path: str) -> list:
    """
    Read a local json file
    :param path: string path to the file
    :return: list[Dictionaries]
    """
    with open(path, 'r') as file:
        data = json.load(file, encoding='utf-8')
    return data


# Read json from a URL
def read_json_url(url: str) -> list:
    """
    Read a json file from a URL
    :param url: string URL to the file
    :return: list[Dictionaries]
    """
    response = requests.get(url)
    json_data = response.json()
    data = json.loads(json_data, encoding='utf-8')
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


# Print data
def print_data(data):
    """
    Refers to the data and prints it:

        <date: 14.10.2018> <description>
        <from: "Visa Platinum 7000 79** **** 6361"> -> <to: "Счет **9638">
        <operationAmount[amount]> <currency[name]>
б.

    :param data:
    :return:
    """
