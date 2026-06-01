import pytest

from src.main import Product, Category


@pytest.fixture
def return_done_js_list():
    return [{"tests": {"hello": "world"}}]


@pytest.fixture
def prod_one():
    return Product(name="Patato", description="very yammy", price=80.0, quantity=10)


@pytest.fixture
def category_first():
    return Category(
        name="Smart tv",
        description="looks great",
        products=[
            Product(name="TV", description="its ok", price=1500.0, quantity=4),
            Product(name="Phone", description="looks great", price=150.0, quantity=10),
        ],
    )


@pytest.fixture
def category_second():
    return Category(
        name="Q-tv",
        description="update",
        products=[Product(name="TV", description="cool", price=50.0, quantity=6)],
    )


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
