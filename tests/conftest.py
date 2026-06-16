import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone

""" fixture, для класса Product """


@pytest.fixture
def product_one():
    """Для проверки позитивной записи класса Product"""
    product_phone_one = Product("Phone", "Favorite", 2500.0, 10)
    return product_phone_one


@pytest.fixture
def product_two():
    """Для проверки позитивной записи класса Product"""
    product_phone_two = Product("Phone", "Smartphone", 4000.0, 4)
    return product_phone_two


@pytest.fixture
def product_three():
    """Для проверки позитивной записи класса Product"""
    product_phone_three = Product("TV", "Smart tv", 20000.0, 3)
    return product_phone_three


@pytest.fixture
def dict_product():
    """Для проверки позитивной распаковки в класс методе Product new_product"""
    return {"name": "Phone", "description": "Nice view", "price": 1500.0, "quantity": 5}


""" fixture, для класса Smartphone наследника класса Product """


@pytest.fixture
def smart_phone_one():
    """Для проверки позитивной записи объекта в класс Smartphone"""
    return Smartphone("Iphone", "Iphone 15 pro max", 50000, 3, 90.5, "Pro max", 512, "Синий")


@pytest.fixture
def smart_phone_two():
    """Для проверки позитивной записи объекта в класс Smartphone"""
    return Smartphone("Iphone", "Iphone 16 pro max", 120000, 1, 100.0, "Pro max", 512, "Фиолетовый")


""" fixture, для класса LawnGrass наследника класса Product """


@pytest.fixture
def lawn_grass_one():
    """Для проверки позитивной записи объекта в класс LawnGrass"""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_two():
    """Для проверки позитивной записи объекта в класс LawnGrass"""
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


""" fixture, для класса Category """


@pytest.fixture
def category_one(product_one):
    """Возвращает объект класса Category"""
    return Category("Mobile phone", "technic", [product_one])


""" fixture, для read_json.py """


@pytest.fixture
def return_done_js_list():
    """Для прочтения файла JSON"""
    return [{"tests": {"hello": "world"}}]


""" fixture, для utils.py """


@pytest.fixture
def list_to_records_class():
    """Для записи из JSON файла в список Product"""
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных "
            "функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]
