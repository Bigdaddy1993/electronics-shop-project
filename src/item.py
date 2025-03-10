import csv
import math


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        """ Возвращает наименование товара. """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """ Устанавливает наименование товара. """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def __repr__(self):
        """

        :return: Магический метод для отображения информации об объекте класса
        (для разработчиков)
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """

        :return: Магический метод для отображения информации об объекте класса
        (для пользователей)
        """
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename):
        """инициализирует экземпляры класса Item данными из файла src/items.csv"""
        cls.all.clear()
        try:
            with open(filename, encoding="windows-1251") as f:
                reader = csv.DictReader(f, delimiter=',')
                for line in reader:
                    if 'name' not in line or 'price' not in line or 'quantity' not in line:
                        raise InstantiateCSVError(f'Файл {filename} поврежден')
                    name = line['name']
                    price = float(line['price'])
                    quantity = cls.string_to_number(line['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {filename}')

    @staticmethod
    def string_to_number(string: str) -> int:
        """Преобразование строки в число"""
        return int(math.floor(float((string.replace(',', '.')))))


class InstantiateCSVError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
