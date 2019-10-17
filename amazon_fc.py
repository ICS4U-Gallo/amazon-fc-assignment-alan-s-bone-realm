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
        self.products_stored = {}
        Compartment.all_compartments.append(self)


def put_products_on_trolly(items: List, trolly: object): #specific trolly
    for item in items:
        for compartment in Compartment.all_compartments:
            if trolly.compartment_number == compartment.number:
                if item.number in compartment.product_numbers:
                    trolly.product_list.append(item)
                    items.remove(item)
                

def put_objects_on_shelf(trolly: object):
    for compartment in Compartment.all_compartments:
        if trolly.compartment_number == compartment.number:
            for product in trolly.product_list:
                if product.name not in compartment.products_stored:
                    compartment.products_stored[product.name] = {"Quantity": 1, "Info": product}
                else:
                    compartment.products_stored[product.name]["Quantity"] += 1
                trolly.product_list.remove(product)



c1 = Compartment(1111, [1, 4])
t1 = Trolly(c1.number)
p1 = Product("bag", 1, "p1.png")
p2 = Product("chair", 3, "p1.png")

item_list = [p1, p2]

put_products_on_trolly(item_list, t1)

print(t1.product_list)
print(item_list)