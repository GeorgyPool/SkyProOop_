import pytest


def test_correct_record_in_class(smart_phone_one):
    """Тест на позитивную запись в атрибуты класса"""
    assert smart_phone_one.name == "Iphone"
    assert smart_phone_one.description == "Iphone 15 pro max"
    assert smart_phone_one.price == 50000
    assert smart_phone_one.quantity == 3
    assert smart_phone_one.efficiency == 90.5
    assert smart_phone_one.model == "Pro max"
    assert smart_phone_one.memory == 512
    assert smart_phone_one.color == "Синий"
    assert smart_phone_one.__str__() == "Iphone, 50000руб, Остаток: 3"


def test_magic_method_add(smart_phone_one, smart_phone_two):
    """Тест на проверку сложения двух одинаковых дочерних классов Smartphone(Product)"""
    result_add = smart_phone_one + smart_phone_two
    assert result_add == 270000


def test_not_correct_magic_method_add(smart_phone_one):
    """Тест, что при, передачи в метод сложения не того класса возникает ошибка TypeError"""
    with pytest.raises(TypeError):
        assert smart_phone_one + 1
