from typing import List, Dict
import random


class Item:
    """Item class

    Attrs:
        product_name (str): The name of the product.
        product_number (int): The product's identification number.
        barcode (int): An integer barcode of the product.
        image (str): The picture of the product.

    """
    unsorted_items = []
    sorted_items = []
    max_barcodes = 1000000
    barcodes = []

    def __init__(self, product_name: str, product_number: int, image: str, length: int, width: int, height: int):
        self.name = product_name
        self.number = product_number
        self.image = image
        self.dimensions = (length, width, height)
        while True:
            if len(Item.barcodes) == Item.max_barcodes:
                Item.max_barcodes *= 10
            else:
                self.barcode = random.randint(0, Item.max_barcodes)
                if self.barcode not in Item.barcodes:
                    Item.barcodes.append(self.barcode)
                    break
        Item.unsorted_items.append(self)


class Shelf:
    """Shelf class

    Attrs:
        all_shelves (List[]): A list containing all the shelves.
        shelf_number (int): An integer of the number of the shelf.
        product_nums (List[int]): A list of unique item identifications numbers.

    """

    all_shelves = []

    def __init__(self, shelf_number: int, product_numbers: List[int]):
        self.number = shelf_number
        self.compartments = []
        for product_number in product_numbers:
            self.compartments.append({"Product Number": product_number, "Quantity": 0, "Items Stored": None})
        Shelf.all_shelves.append(self)


class Cart:
    """Cart/trolly class

    Attrs:
        items_stored: An empty list.
    """

    def __init__(self):
        self.items_stored = []
        self.max_capacity = 100

    def assign_cart(self, shelf: object):
        """Assign the cart object to a shelf object"""
        self.shelf = shelf

    def scan_onto_cart(self):
        """Scan items onto the cart if the cart is assigned to a shelf
        Args:
            items: a list of item objects
        """
        if hasattr(self, "shelf"):
            for item in Item.unsorted_items:
                if len(self.items_stored) < self.max_capacity:
                    for product in self.shelf.compartments:
                        if item.number == product["Product Number"]:
                            self.items_stored.append(item)

    def scan_onto_shelf(self):
        """Scan item object from the trolly into compartments within the shelf"""
        if hasattr(self, "shelf"):
            items_added = []
            for item in self.items_stored:
                for product in self.shelf.compartments:
                    if product["Product Number"] == item.number:
                        if product["Items Stored"] is None:
                            product["Items Stored"] = []
                        product["Items Stored"].append(item)
                        product["Quantity"] += 1
                        items_added.append(item)
                        Item.sorted_items.append(item)
                        Item.unsorted_items.remove(item)
            for item in items_added:
                self.items_stored.remove(item)


class Order:
    all_orders = []

    def __init__(self, number: int, product_num_and_quantity: Dict[int, int]):
        self.number = number
        self.products_needed = product_num_and_quantity
        self.status = "Incomplete"
        Order.all_orders.append(self)


class Bin:
    """Bin class

    Attrs:
        all_bins: An empty list.
        order_number (int): An integer representing the order number.
        product_num_and_quantity (Dict[str, int]): A dictionary taking the product number and quantity.
        items_contained: An empty list.
    """

    all_bins = []

    def __init__(self):
        """Create a bin object

        Args:
            order_number: the order number
            product_num_and_quantity: a dictionary with product numbers as key terms and the quantity of each product as the value
        """
        self.items_contained = []
        self.order = None
        Bin.all_bins.append(self)

    def assign_order(self):
        for order in Order.all_orders:
            if order.status == "Incomplete":
                self.order = order
                self.order.status = "Fulfilling"
                break

    def scan_into_bin(self):
        """Scans items into the bin"""
        for product_number in self.order.products_needed.keys():
            for shelf in Shelf.all_shelves:
                for product in shelf.compartments:
                    if product_number == product["Product Number"]:
                        while product["Quantity"] > 0 and self.order.products_needed[product_number] > 0:
                            self.items_contained.append(product["Items Stored"][0])
                            Item.sorted_items.remove(product["Items Stored"][0])
                            product["Items Stored"].pop(0)
                            self.order.products_needed[product_number] -= 1
                            product["Quantity"] -= 1
                        if self.order.products_needed[product_number] == 0:
                            self.order.products_needed[product_number] = None
                        else:
                            # reserve items that are currently available but order will not be sent out for shipping until order fulfilled for the item
                            items_missing = self.order.products_needed[product_number]
                            print(
                                f"Order Fulfillment Invalid: {items_missing} more items of (product number: {product_number}) needed to complete order.")

        # remove products from order that are scanned into bin
        self.order.products_needed = {item_num: quantity for item_num,
                                quantity in self.order.products_needed.items() if quantity is not None}


class Package:
    """Package class

    Attrs:
        all_packages: An empty list.
        order_num (int): An integer of the order number.
        package_type (str): A string stating the type of package.
        items: An empty list.
        stamped: A boolean value.
    """

    all_packages = []

    def __init__(self, Bin: object, address: str, package_type: str):
        self.order_num = Bin.order.number
        self.bin = Bin
        self.type = package_type
        self.items = []
        self.address = address
        self.stamped = False
        Package.all_packages.append(self)

    def pack_items(self):
        """Put items into the package object"""
        items_packaged = []
        for item in self.bin.items_contained:
            if item.number not in self.bin.order.products_needed.keys():
                self.items.append(item)
                items_packaged.append(item)
        for item in items_packaged:
            self.bin.items_contained.remove(item)
        if len(self.bin.order.products_needed) == 0:
            self.bin.order.status = "Completed"

    @staticmethod
    def send_to_truck():
        """Send package object to the conveyor belt to be taken to the truck
        Args:
            address: the address the package is being sent to
        """
        for package in Package.all_packages:
            if package.bin.order.status == "Completed":
                for truck in Truck.all_trucks:
                    if package.order_num in truck.orders.keys():
                        truck.orders[package.order_num] = package
                        package.stamped = True


class Truck:
    """Truck class

    all_trucks: An empty list.
    truck_number (int): An integer representing the truck number.
    order_list (List[]): A list of all the orders.
    orders: An empty dictionary.
    """

    all_trucks = []

    def __init__(self, truck_number: int, order_list: List):
        self.number = truck_number
        self.orders = {}
        for order in order_list:
            self.orders[order] = None
        Truck.all_trucks.append(self)
