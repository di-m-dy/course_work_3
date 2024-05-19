import pytest
import json
from utils import read_json_local, filter_data, sort_data, set_operations
import config
import os
from transaction import Operation


def test_read_json_local(fx_data_all):
    assert read_json_local(os.path.join(config.TEST_PATH, 'test_operations.json')) == fx_data_all
    pytest.raises(json.JSONDecodeError, read_json_local, os.path.join(config.TEST_PATH, 'test_empty_json.json'))
    pytest.raises(FileNotFoundError, read_json_local, 'test_empty.json')


def test_filter_data(fx_list_operations):
    assert filter_data(fx_list_operations, 'state', 'CANCELED') == [fx_list_operations[3]]
    assert filter_data(fx_list_operations, 'state', 'EXECUTED') == [
        fx_list_operations[0],
        fx_list_operations[1],
        fx_list_operations[2]
    ]
    assert filter_data(fx_list_operations, 'state', 'REVERSED') == []
    assert filter_data(fx_list_operations, 'unknown', 'REVERSED') == []
    assert filter_data([], 'state', 'EXECUTED') == []
    assert isinstance(fx_list_operations[0], Operation)
    assert isinstance(filter_data(fx_list_operations, 'state', 'CANCELED'), list)


def test_sort_data(fx_list_operations):
    assert sort_data(fx_list_operations, limit=3) == [
        fx_list_operations[3],
        fx_list_operations[1],
        fx_list_operations[2]
    ]


def test_set_operations(fx_data_all, fx_list_operations):
    assert set_operations(fx_data_all)[0].get_operation() == fx_list_operations[0].get_operation()
    assert set_operations(fx_data_all)[1].get_operation() == fx_list_operations[1].get_operation()
    assert set_operations(fx_data_all)[2].get_operation() == fx_list_operations[2].get_operation()
    assert set_operations(fx_data_all)[3].get_operation() == fx_list_operations[3].get_operation()
