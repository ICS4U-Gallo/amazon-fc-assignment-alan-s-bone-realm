from typing import List

class Trolly:
    all_trollies = []

    def __init__(self, compartment_number: int):
        self.compartment_number = compartment_number
        self.item_list = []
        Trolly.all_trollies.append(self)
    
    def put_products_on_trolly(self, items: List):
        for item in items:
            for compartment in Compartment.all_compartments:
                if self.compartment_number == compartment.number:
                    if item.number in compartment.product_numbers:
                        self.item_list.append(item)
                        items.remove(item)


class Product:
    def __init__(self, product_name: str, product_number: int, image: str):
        self.name = product_name
        self.number = product_number
        self.image = image
    
    def ship_out(self, address: str, stamp: bool):
        pass


class Compartment:
    all_compartments = []
    def __init__(self, compartment_number: int, product_numbers: List[int]):
        self.number = compartment_number
        self.product_numbers = product_numbers
        self.products_stored = {}
        Compartment.all_compartments.append(self)
                
    def put_objects_on_shelf(self):
        for trolly in Trolly.all_trollies:
            if trolly.compartment_number == self.number:
                for product in trolly.item_list:
                    if product.name not in self.products_stored:
                        self.products_stored[product.name] = {"Quantity": 1, "Item Info": product}
                    else:
                        self.products_stored[product.name]["Quantity"] += 1
                    trolly.item_list.remove(product)



c1 = Compartment(1111, [1, 4])
t1 = Trolly(c1.number)
p1 = Product("Bag", 1, "p1.png")
p2 = Product("Chair", 3, "p1.png")

item_list = [p1, p2]
print(item_list)

t1.put_products_on_trolly(item_list)

print(t1.item_list)
print(item_list)

print(c1.products_stored)
c1.put_objects_on_shelf()
print(c1.products_stored)
print(t1.item_list)

print(c1.products_stored["Bag"]["Item Info"].name)
print(c1.products_stored["Bag"]["Item Info"].number)
print(c1.products_stored["Bag"]["Item Info"].image)

item_list.append(p1)
t1.put_products_on_trolly(item_list)
c1.put_objects_on_shelf()
print(c1.products_stored)