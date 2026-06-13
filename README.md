# ПРОЕКТ ...


## *Модули* :

+ модуль [category.py](src/category.py) содержит класс Product
````
class Product(name=str, description=str, price=float, quantity=int)
методы:

@classmethod
new_products({key:value})

@proprty - возвращает текущий прайс продукта
price -> price

@price.setter - устанавливает новый прайс на продукт
price = 100 
````

+ модуль [category.py](src/category.py) - содержит класс Category
````
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

+ модуль [smartphone.py](src/smartphone.py) - содержит класс Smartphone
````
Класс Smartphone дочерний класс класса Product

class Smartphone(Product)
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
````

+ модуль [lawn_grass.py](src/lawn_grass.py) - содержит класс LawnGrass
````
Класс LawnGrass дочерний класс класса Product

class LawnGrass(product)
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
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
+ [category.py](src/category.py) - [test_category.py](tests/test_category.py)
+ [lawn_grass.py](src/lawn_grass.py) - [test_lawn_grass.py](tests/test_lawn_grass.py)
+ [product.py](src/product.py)[utils.py](src/utils.py) - [test_product.py](tests/test_product.py)
+ [read_json.py](src/read_json.py) - [test_read_json.py](tests/test_read_json.py)
+ [smartphone.py](src/smartphone.py) - [test_smartphone.py](tests/test_smartphone.py)
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
