"""
en: Description: Configuration file for the application
ru: Описание: Файл конфигурации для приложения
"""
import os

# Path to the data file
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data/operations.json')
FILTER_KEY = 'state'
STATUS = 'EXECUTED'
LIMIT_OPERATIONS = 5
