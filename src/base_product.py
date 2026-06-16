from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def new_product(self, dict_prod):
        pass

    @abstractmethod
    def price(self):
        pass
