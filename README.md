# ПРОЕКТ ...


## *Модули* :

+ модуль [main.py](src/main.py) содержит классы
````
class Product(name=str, description=str, price=float, quantity=int)

class Category:
name: str
    description: str
    products: list
    category_count = 0
    product_count
    __init__(name, description, products[list])
````
+ модуль [read_json.py](src/read_json.py) читает JSON-файлы
````
read_file_json(принимает путь до файла и возвращает список python, 
если фаил не найден возвращает пустой список) -> list[dict] | list[]
````
+ модуль [utils.py](src/utils.py) записывает объекты класса Category в список
````
records_class_category(list[dict]) -> list[Category] | list[]-если передан пустой список
````
