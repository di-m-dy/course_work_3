"""
en: Description: Utility functions for the application
ru: Описание: Вспомогательные функции для приложения
"""
import json

import config
from transaction import Operation


# Read local json file
def read_json_local(path: str) -> list:
    """
    Read a local json file
    :param path: string path to the file
    :return: list[Dictionaries]
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return [i for i in data if i]


# Filter data by key
def filter_data(data: list[Operation], key: str, value: str) -> list[Operation]:
    """
    Filter data by key
    :param data: list of dictionaries
    :param key: key of the dictionary
    :param value: value of the key
    :return: new filtered list
    """
    new_data = [operation for operation in data if operation.get_operation().get(key) == value]
    return new_data


# Sort data by key
def sort_data(data: list[Operation], reverse=True, limit=config.LIMIT_OPERATIONS) -> list:
    """
    Sort data
    :param data:
    :param reverse:
    :param limit:
    :return:
    """
    new_data = sorted(data, reverse=reverse)
    if limit:
        new_data = new_data[:limit]
    return new_data


def set_operations(data_base: list[dict]) -> list[Operation]:
    """
    Set operations
    :param data_base: list of dictionaries
    :return: list of Operations
    """
    operations = []
    for data in data_base:
        amount = 'No amount'
        currency_name = 'No currency'
        if isinstance(data.get('operationAmount'), dict):
            amount = data['operationAmount'].get('amount', amount)
            if isinstance(data['operationAmount'].get('currency'), dict):
                currency_name = data['operationAmount']['currency'].get('name', currency_name)
        operation = Operation(
            state=data.get('state', ''),
            date=data.get('date', ''),
            description=data.get('description', ''),
            from_=data.get('from', ''),
            to=data.get('to', ''),
            amount=amount,
            currency_name=currency_name
        )
        operations.append(operation)
    return operations
