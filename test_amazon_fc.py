from amazon_fc import *


def test_Item():
    steak = Item("Steak", 1, "steakpic.jpg", 1, 2, 3)
    assert steak.name == "Steak"
    assert steak.number == 1
    assert steak.image == "steakpic.jpg"

    fish = Item("Fish", 2, "betafish.jpg", 3, 3, 3)
    assert fish.name == "Fish"
    assert fish.number == 2
    assert fish.image == "betafish.jpg"

    alans_left_shoe = Item("Alan Left Shoe", 3, "shoes.jpg", 2, 3, 1)
    assert alans_left_shoe.name == "Alan Left Shoe"
    assert alans_left_shoe.number == 3
    assert alans_left_shoe.image == "shoes.jpg"

    assert len(Item.unsorted_items) == 3


def test_Shelf():
    shelf1 = Shelf(1, [1, 2, 4])
    assert shelf1.number == 1
    assert shelf1.compartments == [{"Product Number": 1, "Quantity": 0, "Items Stored": None}, {
        "Product Number": 2, "Quantity": 0, "Items Stored": None}, {"Product Number": 4, "Quantity": 0, "Items Stored": None}]

    shelf2 = Shelf(3, [3, 5, 10])
    assert shelf2.number == 3
    assert shelf2.compartments == [{"Product Number": 3, "Quantity": 0, "Items Stored": None}, {
        "Product Number": 5, "Quantity": 0, "Items Stored": None}, {"Product Number": 10, "Quantity": 0, "Items Stored": None}]


def test_Cart():
    cart1 = Cart()
    assert cart1.items_stored == []
    cart1.assign_cart(Shelf.all_shelves[0])
    assert hasattr(cart1, "shelf") is True and cart1.shelf.number == 1
    cart1.scan_onto_cart()
    assert len(cart1.items_stored) == 2
    cart1.scan_onto_shelf()
    assert len(cart1.items_stored) == 0
    assert len(Item.sorted_items) == 2
    assert len(Item.unsorted_items) == 1

    cart2 = Cart()
    assert cart2.items_stored == []
    cart2.assign_cart(Shelf.all_shelves[1])
    assert hasattr(cart2, "shelf") is True and cart2.shelf.number == 3
    cart2.scan_onto_cart()
    assert len(cart2.items_stored) == 1
    cart2.scan_onto_shelf()
    assert len(cart2.items_stored) == 0
    assert len(Item.sorted_items) == 3
    assert len(Item.unsorted_items) == 0


def test_Order():
    order1 = Order(1, {1: 1})
    assert order1.number == 1
    assert order1.products_needed == {1: 1}

    order2 = Order(1229, {2: 1})
    assert order2.number == 1229
    assert order2.products_needed == {2: 1}

    order3 = Order(2374, {3: 2})
    assert order3.number == 2374
    assert order3.products_needed == {3: 2}

    assert len(Order.all_orders) == 3


def test_Bin():
    garbagebin = Bin()
    assert garbagebin.items_contained == []
    assert garbagebin in Bin.all_bins
    garbagebin.assign_order()
    assert hasattr(
        garbagebin, "order") is True and garbagebin.order.status == "Fulfilling"
    garbagebin.scan_into_bin()

    alanbin = Bin()
    assert alanbin.items_contained == []
    assert alanbin in Bin.all_bins
    alanbin.assign_order()
    assert hasattr(
        alanbin, "order") is True and alanbin.order.status == "Fulfilling"
    alanbin.scan_into_bin()

    maxbin = Bin()
    assert maxbin.items_contained == []
    assert maxbin in Bin.all_bins
    maxbin.assign_order()
    assert hasattr(
        maxbin, "order") is True and maxbin.order.status == "Fulfilling"
    maxbin.scan_into_bin()
    assert len(maxbin.items_contained) == 1
    assert maxbin.order.products_needed == {3: 1}


def test_Package():
    package1 = Package(Bin.all_bins[0], "Garbage Ave", "Bag")
    assert package1.order_num == 1
    assert package1.type == "Bag"
    assert len(package1.items) == 0
    package1.pack_items()
    assert len(package1.items) == 1
    assert package1.bin.order.status == "Completed"

    package2 = Package(Bin.all_bins[1], "Alan's House", "Bag")
    assert package2.order_num == 1229
    assert package2.type == "Bag"
    assert len(package2.items) == 0
    package2.pack_items()
    assert len(package2.items) == 1
    assert package2.bin.order.status == "Completed"

    package3 = Package(Bin.all_bins[2], "Max's House", "Box")
    assert package3.order_num == 2374
    assert package3.type == "Box"
    assert len(package3.items) == 0
    package3.pack_items()
    assert len(package3.items) == 0
    assert package3.bin.order.status == "Fulfilling"


def test_Truck():
    truck1 = Truck(13, [1, 4, 5, 6, 7])
    assert truck1.number == 13
    assert truck1.orders == {1: None, 4: None, 5: None, 6: None, 7: None}

    truck2 = Truck(232, [1229, 2374])
    assert truck2.number == 232
    assert truck2.orders == {1229: None, 2374: None}

    Package.send_to_truck()
    assert truck1.orders[1] != None
    assert truck2.orders[1229] != None
    assert truck2.orders[2374] == None
