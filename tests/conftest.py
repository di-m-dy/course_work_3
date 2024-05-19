"""
en: Module for fixture
"""
import pytest
import datetime
from transaction import Operation


@pytest.fixture
def fx_data_all():
    """
    data from test_data.json
    :return: list of dictionaries with different states and dates
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
def op_get_operation():
    return [
        {
            'state': "EXECUTED",
            'date': datetime.datetime(2000, 1, 1),
            'description': "Test_Description_1",
            'from': {
                'type': "Card_From",
                'number': "0000000000000000"
            },
            'to': {
                'type': "Card_To",
                'number': "0000000000000000"
            },
            'amount': "0.0",
            'currency_name': "Test_Name_Currency"
        },
{
            'state': "EXECUTED",
            'date': datetime.datetime(2002, 1, 1),
            'description': "Test_Description_2",
            'from': {
                'type': "Card_From",
                'number': "0000000000000000"
            },
            'to': {
                'type': "Счет_To",
                'number': "00000000000000000000"
            },
            'amount': "0.0",
            'currency_name': "Test_Name_Currency"
        },
        {
            'state': "EXECUTED",
            'date': datetime.datetime(2001, 1, 1),
            'description': "Test_Description_3",
            'from': {
                'type': "",
                'number': ""
            },
            'to': {
                'type': "Счет_To",
                'number': "00000000000000000000"
            },
            'amount': "0.0",
            'currency_name': "Test_Name_Currency"
        },
        {
            'state': "CANCELED",
            'date': datetime.datetime(2004, 1, 1),
            'description': "Test_Description_4",
            'from': {
                'type': "Test_From",
                'number': "0000000000000000"
            },
            'to': {
                'type': "Test_To",
                'number': "00000000000000000000"
            },
            'amount': "0.0",
            'currency_name': "Test_Name_Currency"
        }
    ]



