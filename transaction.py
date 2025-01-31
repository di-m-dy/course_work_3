"""
en: Module with the Operation class
ru: Модуль с классом Operation
"""
import datetime
import re
from typing import Optional


class Operation:
    """
    en: Class to represent an operation
    ru: Класс для представления операции
    """
    def __init__(
            self,
            state: str,
            date: str,
            description: str,
            from_: Optional[str],
            to: str,
            amount: str,
            currency_name: str
    ):
        self.state = state
        self.description = description
        self.from_ = from_
        self.to = to
        self.amount = amount
        self.currency_name = currency_name
        try:
            self.date = datetime.datetime.fromisoformat(date)
        except ValueError:
            self.date = None

    def get_operation(self) -> dict:
        """
        en: Get operation data
        ru: Получить данные операции
        :return: 
        """
        data_dict = {
            'state': self.state,
            'date': self.date,
            'description': self.description,
            'from': self.get_type_number(self.from_),
            'to': self.get_type_number(self.to),
            'amount': self.amount,
            'currency_name': self.currency_name
        }
        return data_dict

    @staticmethod
    def get_type_number(string) -> Optional[dict]:
        """
        en: Get type and number
        ru: Получить тип и номер
        :return: dict
        """
        pattern = r"(\D+) (\d+)"
        match = re.search(pattern, string)
        if match:
            type_ = match.group(1).strip()
            number_ = match.group(2).strip()
            return {
                'type': type_ if type_ else '',
                'number': number_ if number_ else ''}
        return None

    @staticmethod
    def number_repr(type_, string) -> str:
        """
        en: Replace private area with '*'
        ru: Заменить приватную область на '*'
        :param type_:
        :param string:
        :return: str
        """
        if type_.startswith('Счет'):
            return f"****************{string[-4:]}"
        string = f"{string[:6]}******{string[12:]}"
        return ' '.join([string[i:i + 4] for i in range(0, len(string), 4)])

    def __str__(self) -> str:
        """
        en: String representation of the object
        ru: Строковое представление объекта
        :return: str
        """
        data = self.get_operation()
        date = data['date'].strftime("%d.%m.%Y") if data['date'] else 'No date'
        description = data['description'] if data['description'] else 'No description'
        #
        from_number = self.number_repr(data['from']['type'], data['from']['number']) if data['from'] else ''
        from_ = f"{data['from']['type']} {from_number}" if data['from'] else ''
        to_number = self.number_repr(data['to']['type'], data['to']['number']) if data['to'] else ''
        to = f"{data['to']['type']} {to_number}" if data['to'] else ''
        delimiter = ' -> ' if (from_ and to) else ''
        ending_line = '\n' if (from_ or to) else ''
        #
        amount = data['amount'] if data['amount'] else 'No amount'
        currency_name = data['currency_name'] if data['currency_name'] else 'No currency'
        # create lines
        line_1 = f"{date} {description}\n"
        line_2 = f"{from_}{delimiter}{to}{ending_line}"
        line_3 = f"{amount} {currency_name}\n"
        lines = f"{line_1}{line_2}{line_3}"
        return lines

    def __gt__(self, other) -> bool:
        """
        en: Compare objects by date of the operation
        ru: Сравнение объектов по дате операции
        """
        return self.date > other.date

    def __lt__(self, other) -> bool:
        """
        en: Compare objects by date of the operation
        ru: Сравнение объектов по дате операции
        """
        return self.date < other.date
