from utils import read_json_local


def test_read_json_local():
    assert read_json_local('data/test_operations.json') == [
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
            "description": "Test_Description",
            "from": "Test_From 0000000000000000",
            "to": "Test_To 00000000000000000000"
        }
    ]


def test_read_json_url():
    pass


def test_filter_data():
    pass


def test_sort_data():
    pass


def test_convert_date():
    pass


def test_split_type_number():
    pass


def test_set_private_string():
    pass


def test_regroup_string():
    pass
