from src.classes import Category, Product


# Тест класса Product
def test_product(prod_one):
    assert prod_one.name == "Patato"
    assert prod_one.description == "very yammy"
    assert prod_one.price == 80.0
    assert prod_one.quantity == 10


# Тест класса Product на работу класс метода - new_product и метода геттера price
def tests_class_method_new_prod():
    item = Product.new_product({"name": "phon", "description": "nice phon", "price": 10.0, "quantity": 5})
    assert item.price == 10.0
    assert item.name == "phon"
    item.price = 20.0
    assert item.price == 20.0


# Тест класса Category
def test_category(category_first, str_category_first, category_second):
    assert category_first.name == "tv"
    assert category_first.description == "ok"
    assert str_category_first == "TV, 1500.0руб, Остаток: 14\n"
    assert str(category_first) == "tv, количество продуктов: 14"

    assert category_first.category_count == 2
    assert category_second.category_count == 2
    assert str(category_second) == "Q-tv, количество продуктов: 6"

    assert category_second.product_count == 3


# Тест класса Category на add_product и геттер products
def test_add_product_category():
    item_1 = Product.new_product({"name": "timer", "description": "nice phon", "price": 10.0, "quantity": 5})
    item_2 = Product.new_product({"name": "helper", "description": "nice phon", "price": 10.0, "quantity": 5})
    cat_one = Category(name="any", description="nice item", products=[item_1])
    cat_one.add_product(item_2)
    assert cat_one.products == "timer, 10.0руб, Остаток: 5\nhelper, 10.0руб, Остаток: 5\n"
    assert item_1 + item_2 == 100
