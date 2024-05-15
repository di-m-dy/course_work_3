# Main module for running the program
import config
import utils


def run(file=config.DATA_PATH, url=None, test=False, count_operations=5):
    """
    Запуск программы
    Run the program
    :param file: path to the file
    :param url: link to the json file
    :param test: if True, use the test file
    :param count_operations: count of operations to display
    """
    # Load data
    if test:
        data = utils.read_json_local(config.TEST_PATH)
    elif url:
        data = utils.read_json_url(url)
    else:
        data = utils.read_json_local(file)
    # Фильтр данных по статусу
    # Filter data
    data = utils.filter_data(data, 'state', 'EXECUTED')

    # Сортировка данных по дате
    # Sort data
    data = utils.sort_data(data, 'date', reverse=True, limit=count_operations)

    # Создание строк для отображения
    # Create lines
    lines_list = []
    for operation in data:
        # for line 1
        date_ = utils.convert_date(operation.get('date', 'No date'))
        description_ = operation.get('description', 'No Description')
        # for line 2
        from_ = operation.get('from', '')
        to_ = operation.get('to', '')
        # for line 3
        operation_amount = operation.get('operationAmount')
        # проверка на словарь чтобы вложенность проверить
        # check if it is a dictionary
        if isinstance(operation_amount, dict):
            amount_ = operation_amount.get('amount')
            if isinstance(operation_amount.get('currency'), dict):
                currency_ = operation_amount.get('currency').get('name')
            else:
                currency_ = None
        else:
            amount_ = None
            currency_ = None

        line_1 = f"{date_} {description_}"
        line_2 = f"{from_}{' -> ' if (from_ and to_) else ''}{to_}"
        line_3 = f"{amount_} {currency_}"
        lines = '\n'.join([line_1, line_2, line_3])
        lines_list.append(lines)
    print('\n\n'.join(lines_list))
