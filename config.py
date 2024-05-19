# Description: Configuration file for the application
import os

# Path to the data file
DATA_PATH = os.path.join(os.path.dirname(__file__), 'secrets/operations.json')
TEST_PATH = os.path.join(os.path.dirname(__file__), 'tests/test_operations.json')
FILTER_KEY = 'state'
STATUS = 'CANCELED'
LIMIT_OPERATIONS = -1