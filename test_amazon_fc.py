import amazon_fc as afc

def test_Item():
    steak = afc.Item("Steak", 234876, 127321, "steakpic.jpg")
    assert steak.name == "Steak"
    assert steak.number == 234876
    assert steak.barcode == 127321
    assert steak.image == "steakpic.jpg"

    fish = afc.Item("Fish", 69420, 647787, "betafish.jpg")
    assert fish.name == "Fish"
    assert fish.number == 69420
    assert fish.barcode == 647787
    assert fish.image == "betafish.jpg"

    alans_left_shoe = afc.Item("Alan Left Shoe", 234876, 4837553, "shoes.jpg")
    assert alans_left_shoe.name == "Alan Left Shoe"
    assert alans_left_shoe.number == 234876
    assert alans_left_shoe.barcode == 4837553
    assert alans_left_shoe.image == "shoes.jpg"

def test_Shelf():
    shelf1 = afc.Shelf(1, [1,2,4])
    assert shelf1.number == 1
    assert shelf1.compartments == {1: {"Quantity": 0, "Items Stored": None}, 2: {"Quantity": 0, "Items Stored": None}, 4: {"Quantity": 0, "Items Stored": None}}

    shelf2 = afc.Shelf(2, [3,7,6])
    assert shelf2.number == 2
    assert shelf2.compartments == {3: {"Quantity": 0, "Items Stored": None}, 7: {"Quantity": 0, "Items Stored": None}, 6: {"Quantity": 0, "Items Stored": None}}

    shelf3 = afc.Shelf(3, [15,5,10])
    assert shelf3.number == 3
    assert shelf3.compartments == {15: {"Quantity": 0, "Items Stored": None}, 5: {"Quantity": 0, "Items Stored": None}, 10: {"Quantity": 0, "Items Stored": None}}

# def test_Cart():


def test_Bin():
    garbagebin = afc.Bin(1, ["1238763", 20])
    assert garbagebin.order_num == 1
    assert garbagebin.products_needed == ["1238763", 20]

    alanbin = afc.Bin(1229, ["3472234", 12])
    assert alanbin.order_num == 1229
    assert alanbin.products_needed == ["3472234", 12]

    maxbin = afc.Bin(2374, ["2355534", 4])
    assert maxbin.order_num == 2374
    assert maxbin.products_needed == ["2355534", 4]

def test_Package():
    hongkong = afc.Package(21, "Wooden")
    assert hongkong.order_num == 21
    assert hongkong.type == "Wooden"

    westham = afc.Package(13, "Balloon")
    assert westham.order_num == 13
    assert westham.type == "Balloon"

    egypt = afc.Package(23, "Steel")
    assert egypt.order_num == 23
    assert egypt.type == "Steel"

def test_Truck():
    truck1 = afc.Truck(13, [1,4,5,6,7])
    assert truck1.number == 13
    assert truck1.orders == {1: None, 4: None, 5: None, 6: None, 7: None}

    truck2 = afc.Truck(232, [34,454,234,54])
    assert truck2.number == 232
    assert truck2.orders == {34: None, 454: None, 234: None, 54: None}

    truck3 = afc.Truck(133, [1,34,454,234])
    assert truck3.number == 133
    assert truck3.orders == {1: None, 34: None, 454: None, 234: None}