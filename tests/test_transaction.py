"""
en: Module for testing the functions of the transaction.py file
ru: Модуль для тестирования функций файла transaction.py
"""
import pytest
import json
from utils import read_json_local, filter_data, sort_data, set_operations
import config
import os
from transaction import Operation


def test_exception_date():
    dict_ = {
        "state": "EXECUTED",
        "date": "000000",
        "amount": "0.0",
        "description": "Test_Description_1",
        "from_": "Card_From 0000000000000000",
        "to": "Card_To 0000000000000000",
        "currency_name": "Test_Name_Currency",
    }
    operation = Operation(**dict_)
    data = operation.get_operation()
    assert not data['date']
    assert operation.number_repr('Card', '0000000000000000') == '0000 00** **** 0000'
    assert operation.number_repr('Счет', '00000000000000000000') == '****************0000'