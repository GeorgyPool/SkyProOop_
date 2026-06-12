import pytest

from src.product import Product
from src.category import Category


# fixture для read_json.py
@pytest.fixture
def return_done_js_list():
    return [{"tests": {"hello": "world"}}]


# fixture для класса Product
@pytest.fixture
def prod_one():
    return Product(name="Patato", description="very yammy", price=80.0, quantity=10)


# fixture для класса Category
@pytest.fixture
def category_first() -> Category:
    pr_1 = Product.new_product({"name": "TV", "description": "its ok", "price": 1500.0, "quantity": 4})
    pr_2 = Product.new_product({"name": "TV", "description": "looks great", "price": 150.0, "quantity": 10})
    cat_1 = Category("tv", "ok", [pr_1])
    cat_1.add_product(pr_2)
    return cat_1


@pytest.fixture
def str_category_first(category_first):
    return category_first.products


@pytest.fixture
def category_second():
    return Category(
        name="Q-tv",
        description="update",
        products=[Product(name="TV", description="cool", price=50.0, quantity=6)],
    )


# fixture для utils.py
@pytest.fixture
def list_to_records_class():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство",
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
