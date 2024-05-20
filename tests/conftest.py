"""
en: Module for fixture
ru: Модуль для фикстур
"""
import pytest

from transaction import Operation


@pytest.fixture
def fx_data_all():
    """
    en: data from test_data.json
    ru: данные из test_data.json
    """
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2000-01-01",
            "operationAmount":
                {
                    "amount": "0.0",
                    "currency":
                        {
                            "name": "Test_Name_Currency",
                            "code": "Test_Code_Currency"
                        }
                },
            "description": "Test_Description_1",
            "from": "Card_From 0000000000000000",
            "to": "Card_To 0000000000000000"
        },
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2002-01-01",
            "operationAmount":
                {
                    "amount": "0.0",
                    "currency":
                        {
                            "name": "Test_Name_Currency",
                            "code": "Test_Code_Currency"
                        }
                },
            "description": "Test_Description_2",
            "from": "Card_From 0000000000000000",
            "to": "Счет_To 00000000000000000000"
        },
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2001-01-01",
            "operationAmount":
                {
                    "amount": "0.0",
                    "currency":
                        {
                            "name": "Test_Name_Currency",
                            "code": "Test_Code_Currency"
                        }
                },
            "description": "Test_Description_3",
            "to": "Счет_To 00000000000000000000"
        },
        {
            "id": 1,
            "state": "CANCELED",
            "date": "2004-01-01",
            "operationAmount":
                {
                    "amount": "0.0",
                    "currency":
                        {
                            "name": "Test_Name_Currency",
                            "code": "Test_Code_Currency"
                        }
                },
            "description": "Test_Description_4",
            "from": "Test_From 0000000000000000",
            "to": "Test_To 00000000000000000000"
        }
    ]


@pytest.fixture
def fx_list_operations():
    """
    en: list of Operation
    ru: список Operation
    """
    op_1 = Operation(
        state="EXECUTED",
        date="2000-01-01",
        description="Test_Description_1",
        from_="Card_From 0000000000000000",
        to="Card_To 0000000000000000",
        amount="0.0",
        currency_name="Test_Name_Currency"
    )
    op_2 = Operation(
        state="EXECUTED",
        date="2002-01-01",
        description="Test_Description_2",
        from_="Card_From 0000000000000000",
        to="Счет_To 00000000000000000000",
        amount="0.0",
        currency_name="Test_Name_Currency"
    )
    op_3 = Operation(
        state="EXECUTED",
        date="2001-01-01",
        description="Test_Description_3",
        to="Счет_To 00000000000000000000",
        from_="",
        amount="0.0",
        currency_name="Test_Name_Currency"
    )
    op_4 = Operation(
        state="CANCELED",
        date="2004-01-01",
        description="Test_Description_4",
        from_="Test_From 0000000000000000",
        to="Test_To 00000000000000000000",
        amount="0.0",
        currency_name="Test_Name_Currency"
    )

    return [op_1, op_2, op_3, op_4]


@pytest.fixture
def fx_canceled_operations():
    """
    en: list of Operation with state CANCELED
    ru: список Operation со статусом CANCELED
    """
    op_4 = Operation(
        state="CANCELED",
        date="2004-01-01",
        description="Test_Description_4",
        from_="Test_From 0000000000000000",
        to="Test_To 00000000000000000000",
        amount="0.0",
        currency_name="Test_Name_Currency"
    )
    return [op_4,]


@pytest.fixture
def fx_dict_for_set_op():
    """
    en: dict for set_operations
    ru: словарь для set_operations
    """
    dict_ = {
        "state": "EXECUTED",
        "date": "2000-01-01",
        "amount": "0.0",
        "description": "Test_Description_1",
        "from_": "Card_From 0000000000000000",
        "to": "Card_To 0000000000000000",
        "currency_name": "Test_Name_Currency",
    }
    return dict_


@pytest.fixture
def fx_output_str():
    """
    en: output string of Operation
    ru: строка вывода Operation
    """
    result = ("01.01.2000 Test_Description_1\n"
              "Card_From 0000 00** **** 0000 -> Card_To 0000 00** **** 0000\n"
              "0.0 Test_Name_Currency\n")
    return result


@pytest.fixture
def fx_empty_dict():
    """
    en: empty dict for set_operations
    ru: пустой словарь для set_operations
    """
    dict_ = {
        "state": "",
        "date": "",
        "amount": "",
        "description": "",
        "from_": "",
        "to": "",
        "currency_name": "",
    }
    return dict_


@pytest.fixture
def fx_output_empty_str():
    """
    en: output string of empty Operation
    ru: строка вывода пустой Operation
    """
    result = ("No date No description\n"
              "No amount No currency\n")

    return result
