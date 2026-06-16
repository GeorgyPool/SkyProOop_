from src.product import Product

""" Тесты для класса Product"""


def test_correct_attribute_product(product_one):
    """Тест на позитивную запись атрибутов класса Product"""
    assert product_one.name == "Phone"
    assert product_one.description == "Favorite"
    assert product_one.price == 2500.0
    assert product_one.quantity == 10

    """ Тест на установку новой цены с помощью Setter price """
    product_one.price = 3500.0
    assert product_one.price == 3500.0


def test_bad_price_set_product(product_one, capsys):
    """Тест, на защиту ценны от нулевого значения
    при попытке установить нулевое значение в Setter price, выводится сообщение, что цена не может быть нулевой
    при этом предыдущая цена остается"""
    product_one.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert product_one.price == 2500.0


def test_correct_class_method_add_new_product(dict_product):
    """Тест на позитивную распаковку из словаря и запись в атрибуты класса Product"""
    unpacking = Product.new_product(dict_product)
    assert unpacking.name == "Phone"
    assert unpacking.description == "Nice view"
    assert unpacking.price == 1500.0
    assert unpacking.quantity == 5


def test_magic_method_str_product(product_one):
    """Тест на корректность вывода магического метода __str__"""
    assert product_one.__str__() == "Phone, 2500.0руб, Остаток: 10"


def test_magic_method_add_product(product_one, product_two):
    """Тест на корректность сложения магического метода __add__"""
    result = product_one + product_two
    assert result == 41000.0
