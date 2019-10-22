from typing import List, Dict


class Product:
    def __init__(self, product_name: str, product_number: int, barcode: int, image: str):
        self.name = product_name
        self.number = product_number
        self.barcode = barcode
        self.image = image


class Compartment:
    all_compartments = []

    def __init__(self, compartment_number: int, product_nums: List[int]):
        self.number = compartment_number
        self.shelves = {}
        for product in product_nums:
            self.shelves[product] = {"Quantity": 0, "Items Stored": None}
        Compartment.all_compartments.append(self)


class Trolly:
    all_trollies = []

    def __init__(self):
        self.items_stored = []
        Trolly.all_trollies.append(self)

    def assign_trolly(self, compartment: object):
        self.compartment = compartment

    def scan_products_onto_trolly(self, items: List):
        if hasattr(self, "compartment"):
            items_added = []
            for item in items:
                if item.number in self.compartment.shelves.keys():
                    self.items_stored.append(item)
                    items_added.append(item)
            for item in items_added:
                items.remove(item)

    def put_items_onto_shelf(self):
        if hasattr(self, "compartment"):
            items_added = []
            for item in self.items_stored:
                if self.compartment.shelves[item.number]["Items Stored"] is None:
                    self.compartment.shelves[item.number]["Items Stored"] = []
                self.compartment.shelves[item.number]["Items Stored"].append(
                    item)
                self.compartment.shelves[item.number]["Quantity"] += 1
                items_added.append(item)
            for item in items_added:
                self.items_stored.remove(item)



class Bin:
    all_bins = []

    def __init__(self, order_number: int, product_num_and_quantity: Dict[str, int]):
        self.order_num = order_number
        # {product_num: quantity} takes in product number in the case of multiple products having the same name
        self.products_needed = product_num_and_quantity
        self.items_contained = []
        Bin.all_bins.append(self)

    def scan_items_into_bin(self):
        for item_num in self.products_needed.keys():
            for compartment in Compartment.all_compartments:
                for product, info in compartment.shelves.items():
                    if item_num == product:
                        while info["Quantity"] > 0 and self.products_needed[item_num] > 0:
                            self.items_contained.append(
                                info["Items Stored"][0])
                            info["Items Stored"].pop(0)
                            self.products_needed[item_num] -= 1
                            info["Quantity"] -= 1
                        if self.products_needed[item_num] == 0:
                            self.products_needed[item_num] = None
                        else:
                            # reserve items that are currently available but order will not be sent out for shipping until order fulfilled for the item
                            items_missing = self.products_needed[item_num]
                            print(
                                f"Order Fulfillment Invalid: {items_missing} more items of (product number: {product}) needed to complete order.")

        # remove products from order that are scanned into bin
        self.products_needed = {item_num: quantity for item_num,
                                quantity in self.products_needed.items() if quantity is not None}


class Package:
    all_packages = []

    def __init__(self, order_num: int, package_type: str):
        self.order_num = order_num
        self.type = package_type
        self.items = []
        self.stamped = False
        Package.all_packages.append(self)

    def pack_items(self):
        items_packaged = []
        for container in Bin.all_bins:
            if container.order_num == self.order_num:
                for item in container.items_contained:
                    if item.number not in container.products_needed.keys():
                        self.items.append(item)
                        items_packaged.append(item)
        for item in items_packaged:
            container.items_contained.remove(item)

    def send_to_truck(self, address: str):
        if len(self.items) != 0:
            for truck in Truck.all_trucks:
                if self.order_num in truck.orders.keys():
                    truck.orders[self.order_num] = self
                    self.address = address
                    self.stamped = True


class Truck:
    all_trucks = []

    def __init__(self, truck_number: int, order_list: List):
        self.number = truck_number
        self.orders = {}
        for order in order_list:
            self.orders[order] = None
        Truck.all_trucks.append(self)


product1 = Product("Bag", 1, 11, "bag.png")
product2 = Product("Chair", 2, 22, "chair.png")
product3 = Product("Pillow", 3, 33, "pillow.png")
product4 = Product("Pillow", 3, 44, "pillow.png")
items = [product1, product2, product3, product4]

compartment1 = Compartment(1111, [1, 3])
# print(compartment1.shelves)

trolly1 = Trolly()

# won't do anything since trolly not assigned to a compartment
trolly1.scan_products_onto_trolly(items)
# print(trolly1.items_stored)
# print(items)

trolly1.assign_trolly(compartment1)

# products can now be scanned onto trolly
trolly1.scan_products_onto_trolly(items)
# print(trolly1.items_stored)
# print(items)

trolly1.put_items_onto_shelf()
# print(compartment1.shelves)
# print(trolly1.items_stored)

bin1 = Bin(123, {1: 4, 3: 2})
# print(bin1.products_needed)
bin1.scan_items_into_bin()
# print(bin1.products_needed)
# print(bin1.items_contained)

package1 = Package(123, "box")
package1.pack_items()
# print(package1.items)
# print(bin1.items_contained)

truck1 = Truck(12, [123, 456])
print(truck1.orders)

package1.send_to_truck("8101 Leslie Street")
print(truck1.orders)
print(truck1.orders[123].address)