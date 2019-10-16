from typing import List

class Trolly:
    all_trollies = []

    def __init__(self, compartment_number: int):
        self.compartment_number = compartment_number
        self.product_list = []
        Trolly.all_trollies.append(self)


class Product:
    def __init__(self, product_name: str, product_number: int, image: str):
        self.name = product_name
        self.number = product_number
        self.image = image


class Compartment:
    all_compartments = []
    def __init__(self, compartment_number: int, product_numbers: List[int]):
        self.number = compartment_number
        self.product_numbers = product_numbers
        self.product_list = []
        Compartment.all_compartments.append(self)


def put_products_on_trolly(trolly):
    pass

def put_objects_on_shelf(trolly: object):
#     for compartment in Compartment.all_compartments:
#         if trolly.compartment_number == compartment.number:
#             for product in trolly.product_list:    
    pass



c1 = Compartment(1111, [1, 4])
t1 = Trolly(c1.number)
p1 = Product("bag", 1, "p1.png")
p2 = Product("chair", 4, "p1.png")

t1.product_list.append(p1)
t1.product_list.append(p2)
print(t1.product_list)

