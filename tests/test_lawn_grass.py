import pytest


def test_correct_record_in_class(lawn_grass_one):
    """Тест на позитивную запись в атрибуты класса"""
    assert lawn_grass_one.name == "Газонная трава"
    assert lawn_grass_one.description == "Элитная трава для газона"
    assert lawn_grass_one.price == 500.0
    assert lawn_grass_one.quantity == 20
    assert lawn_grass_one.country == "Россия"
    assert lawn_grass_one.germination_period == "7 дней"
    assert lawn_grass_one.color == "Зеленый"
    assert lawn_grass_one.__str__() == "Газонная трава, 500.0руб, Остаток: 20"


def test_magic_method_add(lawn_grass_one, lawn_grass_two):
    """Тест на проверку сложения двух одинаковых дочерних классов Smartphone(Product)"""
    add_result = lawn_grass_one + lawn_grass_two
    assert add_result == 16750.0


def test_not_correct_magic_method(lawn_grass_one):
    """Тест, что при, передачи в метод сложения не того класса возникает ошибка TypeError"""
    with pytest.raises(TypeError):
        assert lawn_grass_one + 1
