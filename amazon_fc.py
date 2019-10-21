from typing import List, Dict


class Trolly:
    all_trollies = []

    def __init__(self, assigned_compartment_number: int):
        self.number = assigned_compartment_number
        self.item_list = []
        Trolly.all_trollies.append(self)

    def scan_products_onto_trolly(self, items: List):
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
                    self.shelves[product.name] = {
                        "Quantity": 0, "Items Stored": None}
        Compartment.all_compartments.append(self)

    def put_items_onto_shelf(self):
        for trolly in Trolly.all_trollies:  # looks for the assigned trolly
            if trolly.number == self.number:
                for item in trolly.item_list:
                    for product, info in self.shelves.items():
                        if item.name == product:
                            if info["Items Stored"] == None:
                                info["Items Stored"] = []

                            info["Items Stored"].append(item)
                            info["Quantity"] += 1
                            trolly.item_list.remove(item)


class Bin:
    def __init__(self, order_number, product_and_quantity: Dict[str, int]):
        self.order_num = order_number
        self.products_needed = product_and_quantity    # product_name: quantity
        self.items_contained = []

    def scan_items_into_bin(self):
        for item_name in self.products_needed.keys():
            for compartment in Compartment.all_compartments:
                for product in compartment.shelves.keys():
                    if item_name == product:
                        while compartment.shelves[product]["Quantity"] > 0 and self.products_needed[item_name] > 0:
                            self.items_contained.append(
                                compartment.shelves[product]["Items Stored"][0])
                            self.products_needed[item_name] -= 1
                            compartment.shelves[product]["Quantity"] -= 1
                            compartment.shelves[product]["Items Stored"].pop(0)

                        if len(compartment.shelves[product]["Items Stored"]) == 0:
                            compartment.shelves[product]["Items Stored"] = None
                        if self.products_needed[item_name] == 0:
                            self.products_needed[item_name] = None
                        else:
                            print(
                                f"{item_name} out of stock, {self.products_needed[item_name]} more needed.")

        self.products_needed = {item: quantity for item,
                                quantity in self.products_needed.items() if quantity is not None}


p1 = Product("Bag", 1, "p1.png")    # product 1
p2 = Product("Chair", 3, "p1.png")  # product 2
c1 = Compartment(1111, [1, 4])      # new compartment
t1 = Trolly(c1.number)              # new trolly

item_list = [p1, p2]                # put products into a list to be sent out
print(item_list)

# use class function to put items onto trolly, based on trolly destination
t1.scan_products_onto_trolly(item_list)

print(t1.item_list)
print(item_list)

print(c1.shelves)
c1.put_items_onto_shelf()            # put item on shelf
print(c1.shelves)
print(t1.item_list)

print(c1.shelves["Bag"]["Items Stored"][0].name)
print(c1.shelves["Bag"]["Items Stored"][0].number)
print(c1.shelves["Bag"]["Items Stored"][0].image)

item_list.append(p1)
t1.scan_products_onto_trolly(item_list)
c1.put_items_onto_shelf()
print(c1.shelves)

b1 = Bin(111, {"Bag": 5})
print(b1.products_needed)
b1.scan_items_into_bin()
print(b1.products_needed)
print(b1.items_contained)
print(c1.shelves)
