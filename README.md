# ПРОЕКТ ...


## *Модули* :

+ модуль [classes.py](src/classes.py) содержит классы
````
class Product(name=str, description=str, price=float, quantity=int)
методы:

@classmethod
new_products({key:value})

@proprty - возвращает текущий прайс продукта
price -> price

@price.setter - устанавливает новый прайс на продукт
price = 100 

class Category:
name: str
    description: str
    __products: list
    category_count = 0
    product_count
    __init__(name, description, products[list])
методы:

add_product(prod) - добавляет новй продукт к уже существуещему списку в текущей категории объекта

@property
products - возвращает строки из списака Category.__products[list]
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

# ПАПКА TESTS:
Содержит тесты для модулей:
+ [classes.py](src/classes.py) - [test_classes.py](tests/test_classes.py)
+ [read_json.py](src/read_json.py) - [test_read_json.py](tests/test_read_json.py)
+ [utils.py](src/utils.py) - [test_utils.py](tests/test_utils.py)
````
для запуска тестов установить pytest:
pip install pytest
pip install pytest-cov

или :
poetry add --group dev pytest
poetry add --group dev pytest-cov

запуск тестов прописать в терминале: pytest
для запуска конкретного теста: pytest directory/modul.py
для запуска тестов с процентом покрытия: pytest --cov
для запуска тестов с процентом покрытия в html формате: pytest --cov=modul --cov-report=html
````
