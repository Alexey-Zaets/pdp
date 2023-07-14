from abc import ABC, abstractmethod


class Builder(ABC):

    @property
    @abstractmethod
    def product(self):
        raise NotImplementedError

    @abstractmethod
    def produce_first_part(self):
        raise NotImplementedError

    @abstractmethod
    def produce_second_part(self):
        raise NotImplementedError


class Product:

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)


class ConcreteBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_first_part(self):
        self._product.add("First part")

    def produce_second_part(self):
        self._product.add("Second part")


if __name__ == '__main__':
    builder = ConcreteBuilder()
    builder.produce_first_part()
    builder.produce_second_part()
    print(builder.product.parts)
