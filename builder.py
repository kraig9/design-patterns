class Product:
    def __init__(self):
        self.part_a = None
        self.part_b = None

    def __str__(self):
        return f"Part A: {self.part_a}, Part B: {self.part_b}"


class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_product(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.part_a = "Part A1"

    def build_part_b(self):
        self.product.part_b = "Part B1"

    def get_product(self):
        return self.product


class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.part_a = "Part A2"

    def build_part_b(self):
        self.product.part_b = "Part B2"

    def get_product(self):
        return self.product


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()


# Usage example
builder1 = ConcreteBuilder1()
director1 = Director(builder1)
director1.construct()
product1 = builder1.get_product()
print(product1)  # Output: Part A: Part A1, Part B: Part B1

builder2 = ConcreteBuilder2()
director2 = Director(builder2)
director2.construct()
product2 = builder2.get_product()
print(product2)  # Output: Part A: Part A2, Part B: Part B2