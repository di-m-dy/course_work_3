"""
en: Main module for running the widget
ru: Главный модуль для запуска виджета
"""
import utils
import config


def main():
    # en: Load the data / ru: Загрузить данные
    data = utils.read_json_local(config.TEST_PATH)
    # en: Set operations / ru: Установить операции
    operations = utils.set_operations(data)
    # en: Filter the data / ru: Отфильтровать данные
    data = utils.filter_data(operations, config.FILTER_KEY, config.STATUS)
    # en: Sort the data / ru: Отсортировать данные
    data = utils.sort_data(data, 'date')
    # en: Print the data / ru: Вывести данные
    data = '\n'.join([str(operation) for operation in data])
    # en: Print the description / ru: Вывести описание
    if config.LIMIT_OPERATIONS == 1:
        last_str = "Последняя операция"
    elif config.LIMIT_OPERATIONS > -1:
        last_str = f"Все операции"
    else:
        last_str = f"Последние операции"
    print(f"{last_str} со статусом {config.STATUS}:")
    print('-' * 50)
    print(data)


if __name__ == '__main__':
    main()
