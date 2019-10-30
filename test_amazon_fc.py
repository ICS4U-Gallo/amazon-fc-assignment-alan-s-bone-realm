from amazon_fc import *


def test_Item():
    steak = Item("Steak", 234876, 127321, "steakpic.jpg", 1, 2, 3)
    assert steak.name == "Steak"
    assert steak.number == 234876
    assert steak.barcode == 127321
    assert steak.image == "steakpic.jpg"

    fish = Item("Fish", 69420, 647787, "betafish.jpg", 3, 3, 3)
    assert fish.name == "Fish"
    assert fish.number == 69420
    assert fish.barcode == 647787
    assert fish.image == "betafish.jpg"

    alans_left_shoe = Item("Alan Left Shoe", 234876, 4837553, "shoes.jpg", 2, 3, 1)
    assert alans_left_shoe.name == "Alan Left Shoe"
    assert alans_left_shoe.number == 234876
    assert alans_left_shoe.barcode == 4837553
    assert alans_left_shoe.image == "shoes.jpg"


def test_Shelf():
    shelf1 = Shelf(1, [1, 2, 4])
    assert shelf1.number == 1
    assert shelf1.compartments == {1: {"Quantity": 0, "Items Stored": None}, 2: {
        "Quantity": 0, "Items Stored": None}, 4: {"Quantity": 0, "Items Stored": None}}

    shelf2 = Shelf(2, [3, 7, 6])
    assert shelf2.number == 2
    assert shelf2.compartments == {3: {"Quantity": 0, "Items Stored": None}, 7: {
        "Quantity": 0, "Items Stored": None}, 6: {"Quantity": 0, "Items Stored": None}}

    shelf3 = Shelf(3, [15, 5, 10])
    assert shelf3.number == 3
    assert shelf3.compartments == {15: {"Quantity": 0, "Items Stored": None}, 5: {
        "Quantity": 0, "Items Stored": None}, 10: {"Quantity": 0, "Items Stored": None}}


def test_Cart():
    cart1 = Cart()
    assert cart1.items_stored == []

    cart2 = Cart()
    assert cart2.items_stored == []
    
    cart3 = Cart()
    assert cart3.items_stored == []


def test_Order():
    order1 = Order(1, ["1238763", 20])
    assert order1.number == 1
    assert order1.products_needed == ["1238763", 20]

    order2 = Order(1229, ["3472234", 12])
    assert order2.number == 1229
    assert order2.products_needed == ["3472234", 12]

    order3 = Order(2374, ["2355534", 4])
    assert order3.number == 2374
    assert order3.products_needed == ["2355534", 4]

def test_Bin():
    garbagebin = Bin()
    assert garbagebin.items_contained == []
    assert garbagebin in Bin.all_bins

    alanbin = Bin()
    assert alanbin.items_contained == []
    assert alanbin in Bin.all_bins

    maxbin = Bin()
    assert maxbin.items_contained == []
    assert maxbin in Bin.all_bins


def test_Package():
    pass


def test_Truck():
    truck1 = Truck(13, [1, 4, 5, 6, 7])
    assert truck1.number == 13
    assert truck1.orders == {1: None, 4: None, 5: None, 6: None, 7: None}

    truck2 = Truck(232, [34, 454, 234, 54])
    assert truck2.number == 232
    assert truck2.orders == {34: None, 454: None, 234: None, 54: None}

    truck3 = Truck(133, [1, 34, 454, 234])
    assert truck3.number == 133
    assert truck3.orders == {1: None, 34: None, 454: None, 234: None}
