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
