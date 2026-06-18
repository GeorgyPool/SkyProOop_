from src.product import Product


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
        if isinstance(prod, Product):
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
        else:
            raise TypeError

    @property
    def products(self):
        prod = ""
        for pr in self.__products:
            prod += f"{str(pr)}\n"
        return prod

    def __str__(self):
        count_prod = sum(x.quantity for x in self.__products)
        return f"{self.name}, количество продуктов: {count_prod}"

    def middle_price(self):
        try:
            avg_result = sum(x.price for x in self.__products) // len(self.__products)
            return avg_result
        except ZeroDivisionError:
            return 0
