"""
en: Main module for running the widget
ru: Главный модуль для запуска виджета
"""
import utils
import config
import json


def main():
    # en: Load the data / ru: Загрузить данные
    try:
        data = utils.read_json_local(config.DATA_PATH)
    # en: if the file is empty or does not exist / ru: если файл пустой или не существует
    except FileNotFoundError:
        print("Файл не найден")
        exit(1)
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON")
        exit(1)

    # en: Set operations / ru: Установить операции
    operations = utils.set_operations(data)

    # en: Filter the data / ru: Отфильтровать данные
    data = utils.filter_data(operations, config.FILTER_KEY, config.STATUS)

    # en: Sort the data / ru: Отсортировать данные
    data = utils.sort_data(data, 'date')

    # en: Create var of complete data / ru: Создаем переменную сформированных данных
    data = '\n'.join([str(operation) for operation in data])
    # en: Creat var for head of output / ru: Создаем переменную для заголовка вывода
    if config.LIMIT_OPERATIONS == 1:
        last_str = "Последняя операция"
    elif config.LIMIT_OPERATIONS > -1:
        last_str = f"Все операции"
    else:
        last_str = f"Последние операции"
    # en: Output the data / ru: Выводим данные
    print(f"{last_str} со статусом {config.STATUS}:")
    print('-' * 50)
    print(data)


if __name__ == '__main__':
    main()
