import pytest

from src.category import Category

""" Тесты для класса Category """


def test_category_record_correct_result(product_one, product_three):
    """Тест на то что атрибуты класса Category записываются корректно"""
    Category.category_count = 0
    Category.product_count = 0
    category_result = Category("Technic", "набор техники", [product_one, product_three])
    assert category_result.name == "Technic"
    assert category_result.description == "набор техники"

    """ Выводит все товары из переданного списка в виде строки """
    assert isinstance(category_result.products, str)
    assert category_result.products == "Phone, 2500.0руб, Остаток: 10\nTV, 20000.0руб, Остаток: 3\n"

    """ Проверяет что общее количество объектов Category, прибавляется """
    assert Category.category_count == 1

    """ Проверяет что длина списка категории равна длине списка """
    assert category_result.product_count == 2


def test_add_new_product(product_two, product_three):
    """Тест на добавление нового продукта в список"""
    Category.category_count = 0
    Category.product_count = 0
    category_smash = Category("Техника", "Повседневная техника", [product_two])
    assert category_smash.product_count == 1
    category_smash.add_product(product_three)
    assert category_smash.product_count == 2
    assert category_smash.category_count == 1


def test_add_copy_category(product_one, product_two):
    """Тест, что при, передачи продукта с
    таким же именем которое уже есть в списке продуктов суммируется количество продукта"""
    Category.category_count = 0
    Category.product_count = 0
    category_phone = Category("Phone", "Smart phon", [product_one])
    assert category_phone.products == "Phone, 2500.0руб, Остаток: 10\n"
    category_phone.add_product(product_two)
    assert category_phone.products == "Phone, 4000.0руб, Остаток: 14\n"
    assert category_phone.category_count == 1


def test_magic_method_str(product_one, product_two):
    """Тест магического метода str"""
    Category.category_count = 0
    Category.product_count = 0
    category_str = Category("Phones", "Mobile Phones", [product_one, product_two])
    assert category_str.__str__() == "Phones, количество продуктов: 14"
    assert str(category_str) == "Phones, количество продуктов: 14"


def test_not_correct_type_add(category_one):
    """Тест, что при добавлении в список объекта Category возникает ошибка TypeError если
    передан не класс Product или его
    дочерний класс"""
    with pytest.raises(TypeError):
        assert category_one.add_product([])


def test_middle_price_product_correct(product_one, product_two):
    """Тест на положительный результат от получения средней суммы в списке продуктов self.__products"""
    cat1 = Category("Phone", "Телефон в современном мире очень востребован", [product_one, product_two])
    assert cat1.middle_price() == 3250.0


def test_middle_price_product_is_zero_division():
    """Тест что, при, передачи пустого списка в атрибут products возвращает 0"""
    cat1 = Category("Phone", "Телефон в современном мире очень востребован", [])
    assert cat1.middle_price() == 0
