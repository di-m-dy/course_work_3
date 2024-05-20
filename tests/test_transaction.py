"""
en: Module for testing the functions of the transaction.py file
ru: Модуль для тестирования функций файла transaction.py
"""
import pytest

from transaction import Operation


def test_exception_date():
    """
    en: Test for the exception if string for datetime is incorrect
    ru: Тест на исключение, если строка для datetime некорректна
    """
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


def test_str_repr(fx_dict_for_set_op, fx_empty_dict, fx_output_str, fx_output_empty_str):
    """
    en: Test for the string representation of the operation
    ru: Тест на строковое представление операции
    """
    dict_all = fx_dict_for_set_op
    operation_all = Operation(**dict_all)
    dict_empty = fx_empty_dict
    operation_empty = Operation(**dict_empty)
    assert str(operation_all) == fx_output_str
    assert str(operation_empty) == fx_output_empty_str


def test_compare_operations(fx_list_operations):
    """
    en: Test for comparing operations
    ru: Тест на сравнение операций
    """
    op_1 = fx_list_operations[0]
    op_2 = fx_list_operations[1]
    assert op_1 < op_2
    assert op_2 > op_1
    assert op_1 == op_1
    assert op_2 == op_2
    assert op_1 != op_2
