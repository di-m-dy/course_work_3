# Description: Configuration file for the application
import os

# Path to the data file
DATA_PATH = os.path.join(os.path.dirname(__file__), 'secrets/operations.json')
TEST_PATH = os.path.join(os.path.dirname(__file__), 'tests/data_test')
FILTER_KEY = 'state'
STATUS = 'EXECUTED'
LIMIT_OPERATIONS = 10