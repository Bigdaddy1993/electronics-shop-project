from src.item import Item


class Mixin:
    """
    Класс миксин, позволяет изменить язык
    """
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"


class Keyboard(Item, Mixin):
    """
    Класс для клавиатуры
    """
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        Mixin.__init__(self)

    def __str__(self):
        return f'{self.name}'
