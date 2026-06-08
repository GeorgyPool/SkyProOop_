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
