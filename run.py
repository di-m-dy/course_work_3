# Module for running the program
import argparse
from main import run

# Добавление аргументов в парсер
# Add arguments to the parser
parser = argparse.ArgumentParser(description="Виджет «Операции по счетам» "
                                             "для отображения последних операций по счетам")
# Аргумент: количество операций для отображения
# Argument for the number of operations to display
parser.add_argument("--count", type=int, help="Последние N операций по счетам", default=5)
# Взаимоисключаемые необязательные аргументы
# Add mutually exclusive group
group = parser.add_mutually_exclusive_group()
group.add_argument("--file", type=str, help="Путь к файлу json данных")
group.add_argument("--from-url", type=str, help="URL json данных")
group.add_argument("--test", help="Тест с пустым предустановленным файлом json", action='store_true')
# Парсинг аргументов
# Parse arguments
args = parser.parse_args()

if __name__ == '__main__':
    if args.test:
        run(test=True, count_operations=args.count)
    elif args.from_url:
        run(url=args.from_url, count_operations=args.count)
    elif args.file:
        run(file=args.file, count_operations=args.count)
    else:
        run(count_operations=args.count)
