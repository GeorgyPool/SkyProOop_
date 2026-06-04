def test_product(prod_one):
    assert prod_one.name == "Patato"
    assert prod_one.description == "very yammy"
    assert prod_one.price == 80.0
    assert prod_one.quantity == 10


def test_category_first(category_first, category_second):
    assert category_first.name == "Smart tv"
    assert category_first.description == "looks great"
    assert len(category_first.products) == 2

    assert category_first.category_count == 2
    assert category_second.category_count == 2

    assert category_second.product_count == 3
