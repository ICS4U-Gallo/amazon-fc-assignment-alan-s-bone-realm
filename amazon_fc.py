from typing import List

class Trolly:
    all_trollies = []

    def __init__(self, assigned_compartment_number: int):
        self.number = assigned_compartment_number
        self.item_list = []
        Trolly.all_trollies.append(self)
    
    def put_products_on_trolly(self, items: List):
        for item in items:
            for compartment in Compartment.all_compartments:
                if self.number == compartment.number:
                    if item.number in compartment.product_numbers:
                        self.item_list.append(item)
                        items.remove(item)


class Product:
    all_products = []
    def __init__(self, product_name: str, product_number: int, image: str):
        self.name = product_name
        self.number = product_number
        self.image = image
        Product.all_products.append(self)
    
    def ship_out(self, address: str, stamp: bool):
        pass


class Compartment:
    all_compartments = []
    def __init__(self, compartment_number: int, product_numbers: List[int]):
        self.number = compartment_number
        self.product_numbers = product_numbers
        self.shelves = {}
        for number in product_numbers:
            for product in Product.all_products:
                if product.number == number:
                    self.shelves[product.name] = {"Quantity": 0, "Item Info": product}
        Compartment.all_compartments.append(self)
             
                
    def put_objects_on_shelf(self):
        for trolly in Trolly.all_trollies:
            if trolly.number == self.number:
                for item in trolly.item_list:
                    for product, info in self.shelves.items():
                        if item.name == product:
                            info["Quantity"] += 1
                            trolly.item_list.remove(item)



p1 = Product("Bag", 1, "p1.png")    # product 1
p2 = Product("Chair", 3, "p1.png")  # product 2
c1 = Compartment(1111, [1, 4])      # new compartment
t1 = Trolly(c1.number)              # new trolly

item_list = [p1, p2]                # put products into a list to be sent out
print(item_list)

t1.put_products_on_trolly(item_list) # use class function to put items onto trolly, based on trolly destination

print(t1.item_list)
print(item_list)

print(c1.shelves)
c1.put_objects_on_shelf()            # put item on shelf
print(c1.shelves)
print(t1.item_list)

print(c1.shelves["Bag"]["Item Info"].name)
print(c1.shelves["Bag"]["Item Info"].number)
print(c1.shelves["Bag"]["Item Info"].image)

item_list.append(p1)
t1.put_products_on_trolly(item_list)
c1.put_objects_on_shelf()
print(c1.shelves)