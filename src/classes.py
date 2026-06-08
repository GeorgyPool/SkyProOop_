class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_prod):
        return cls(**dict_prod)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, amount):
        if amount <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif amount < self.__price:
            user_input = input("введите 'y' для подтверждения: ").lower()
            if user_input == "y":
                self.__price = amount
        else:
            self.__price = amount

    def __str__(self):
        return f"{self.name}, {self.__price}руб, Остаток: {self.quantity}"

    def __add__(self, other):
        result = self.__price * self.quantity + other.__price * other.quantity
        return result


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, prod):
        find = False
        for pr in self.__products:
            if pr.name == prod.name:
                pr.quantity += prod.quantity
                pr.price = max(pr.price, prod.price)
                find = True
                break
        if not find:
            self.__products.append(prod)
        Category.product_count += 1

    @property
    def products(self):
        prod = ""
        for pr in self.__products:
            prod += f"{pr.name}, {pr.price}руб, Остаток: {pr.quantity}\n"
        return prod

    def __str__(self):
        count_prod = sum(x.quantity for x in self.__products)
        return f"{self.name}, количество продуктов: {count_prod}"


#доп задание:
class IteratorCategory:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data._Category__products):
            result = self.data._Category__products[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration