import os

from src.category import Category
from src.product import Product
from src.read_json import read_file_json


def records_class_category(list_info: list[dict]) -> list[Category]:
    """Принимает на вход список словарей и возвращает
    список объектов класса Category, если список пуст то возвращает пустой список"""

    if list_info:
        user = []
        for info in list_info:
            products = []
            for prod in info["products"]:
                products.append(Product(**prod))
            info["products"] = products
            user.append(Category(**info))
        return user
    else:
        return []


if __name__ == "__main__":
    print(records_class_category(read_file_json(os.path.join("..", "data", "products.json"))))
