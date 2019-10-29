from typing import List, Dict


class Item:
    """Item class

    Attrs:
        product_name (str): The name of the product.
        product_number (int): The product's identification number.
        barcode (int): An integer barcode of the product.
        image (str): The picture of the product.

    """

    def __init__(self, product_name: str, product_number: int, barcode: int, image: str, length: int, width: int, height: int):
        self.name = product_name
        self.number = product_number
        self.barcode = barcode
        self.image = image
        self.dimensions = (length, width, height)


class Shelf:
    """Shelf class

    Attrs:
        all_shelves (List[]): A list containing all the shelves.
        shelf_number (int): An integer of the number of the shelf.
        product_nums (List[int]): A list of unique item identifications numbers.

    """

    all_shelves = []

    def __init__(self, shelf_number: int, product_nums: List[int]):
        self.number = shelf_number
        self.compartments = {}
        for item in product_nums:
            self.compartments[item] = {"Quantity": 0, "Items Stored": None}
        Shelf.all_shelves.append(self)


class Cart:
    """Cart/trolly class

    Attrs:
        items_stored: An empty list.
    """

    def __init__(self):
        self.items_stored = []

    def assign_cart(self, shelf: object):
        """Assign the cart object to a shelf object"""
        self.shelf = shelf

    def scan_onto_cart(self, items: List[object]):
        """Scan items onto the cart if the cart is assigned to a shelf
        Args:
            items: a list of item objects
        """
        if hasattr(self, "shelf"):
            items_added = []
            for item in items:
                if item.number in self.shelf.compartments.keys():
                    self.items_stored.append(item)
                    items_added.append(item)
            for item in items_added:
                items.remove(item)

    def scan_onto_shelf(self):
        """Scan item object from the trolly into compartments within the shelf"""
        if hasattr(self, "shelf"):
            items_added = []
            for item in self.items_stored:
                if self.shelf.compartments[item.number]["Items Stored"] is None:
                    self.shelf.compartments[item.number]["Items Stored"] = []
                self.shelf.compartments[item.number]["Items Stored"].append(
                    item)
                self.shelf.compartments[item.number]["Quantity"] += 1
                items_added.append(item)
            for item in items_added:
                self.items_stored.remove(item)


class Order:
    all_orders = {}

    def __init__(self, number: int, product_num_and_quantity: Dict[int, int]):
        self.number = number
        self.products_needed = product_num_and_quantity
        Order.all_orders[self.number]: "Incomplete"


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
        Bin.all_bins.append(self)

    def assign_order(self, order: object):
        self.order = order

    def scan_into_bin(self):
        """Scans items into the bin"""
        for item_num in self.order.products_needed.keys():
            for shelf in Shelf.all_shelves:
                for product, info in shelf.compartments.items():
                    if item_num == product:
                        while info["Quantity"] > 0 and self.order.products_needed[item_num] > 0:
                            self.items_contained.append(
                                info["Items Stored"][0])
                            info["Items Stored"].pop(0)
                            self.order.products_needed[item_num] -= 1
                            info["Quantity"] -= 1
                        if self.order.products_needed[item_num] == 0:
                            self.order.products_needed[item_num] = None
                        else:
                            # reserve items that are currently available but order will not be sent out for shipping until order fulfilled for the item
                            items_missing = self.order.products_needed[item_num]
                            print(
                                f"Order Fulfillment Invalid: {items_missing} more items of (product number: {product}) needed to complete order.")

        # remove products from order that are scanned into bin
        self.products_needed = {item_num: quantity for item_num,
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

    def __init__(self, Bin: object, package_type: str):
        self.order_num = Bin.order.number
        self.bin = Bin
        self.type = package_type
        self.items = []
        self.stamped = False
        Package.all_packages.append(self)

    def pack_items(self):
        """Put items into the package object"""
        items_packaged = []
        for item in self.bin.items_contained:
            if item.number not in self.bin.products_needed.keys():
                self.items.append(item)
                items_packaged.append(item)
        for item in items_packaged:
            self.bin.items_contained.remove(item)

    def send_to_truck(self, address: str):
        """Send package object to the conveyor belt to be taken to the truck
        Args:
            address: the address the package is being sent to
        """
        if len(self.items) != 0:
            for truck in Truck.all_trucks:
                if self.order_num in truck.orders.keys():
                    truck.orders[self.order_num] = self
                    self.address = address
                    self.stamped = True


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
