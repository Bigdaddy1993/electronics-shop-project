import pytest

from src.item import Item, InstantiateCSVError

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10000


@pytest.fixture
def item_notebook():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price_notebook(item_notebook):
    assert item_notebook.calculate_total_price() == 100000


def test_apply_discount_notebook(item_notebook):
    item_notebook.apply_discount()
    assert item_notebook.price == 20000


def test_name_setter():
    item = Item('Компьютер', 100, 2)
    assert item.name == 'Компьютер'


def test_instantiate_from_csv():
    file_csv = "Смартфон,100,1\nНоутбук, 1000, 3\n"
    with open("test_items.csv", "w", encoding="utf-8") as f:
        f.write(file_csv)


def test_main():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('items.csv')


def test_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('test_items.csv')
