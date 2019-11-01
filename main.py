import amazon_fc as afc
import arcade
import random

screen_width = 800
screen_height = 600


iphone = afc.Item.iphone()
steak = afc.Item.steak()
fish = afc.Item.fish()
shoe = afc.Item.alans_left_shoe()

food_shelf = afc.Shelf([2, 12415])
tech_shelf = afc.Shelf([100])
footwear_shelf = afc.Shelf([3])

cart1 = afc.Cart()
cart1.assign_cart(food_shelf)
cart2 = afc.Cart()
cart2.assign_cart(tech_shelf)
cart3 = afc.Cart()
cart3.assign_cart(footwear_shelf)


clicked_prev = False
clicked_next = False
clicked_shipment = False

clicked_order_fulfillment = False
clicked_ship_out = False
clicked_add_to_cart = False


item = 0



class drawings:
    def __init__(self, name: str, dimensions: tuple):
        self.name = name
        self.dimensions = dimensions

    def prev(self):
        arcade.draw_rectangle_outline(50, 300, 50, 50, arcade.color.WHITE)
        arcade.draw_text("PREV", 50, 300, arcade.color.WHITE, 10,
                         200, "center", 'Arial', True, False, "center", "center")

    def next(self):
        arcade.draw_rectangle_outline(750, 300, 50, 50, arcade.color.WHITE)
        arcade.draw_text("NEXT", 750, 300, arcade.color.WHITE, 10,
                         200, "center", 'Arial', True, False, "center", "center")

    def box_item(self, name: str, dimensions: tuple):
        arcade.draw_rectangle_outline(400, 300, 200, 200, arcade.color.WHITE)
        arcade.draw_text(self.name, 400, 300, arcade.color.WHITE, 20,
                         200, "center", 'Arial', True, False, "center", "center")
        arcade.draw_text(f"{self.dimensions[0]} cm x {self.dimensions[1]} cm x "
                         f"{self.dimensions[2]} cm", 400, 225, arcade.color.WHITE,
                         10, 200, "center", 'Arial', True, False, "center", "center")
        arcade.draw_text(f"Item {item + 1}", 400, 450, arcade.color.WHITE,
                         20, 200, "center", 'Arial', True, False, "center", "center")

    def shipment(self):
        arcade.draw_rectangle_outline(700, 50, 50, 50, arcade.color.WHITE)
        arcade.draw_text("SHIPMENT", 700, 50, arcade.color.WHITE, 8, 200,
                         "center", 'Arial', True, False, "center", "center")

    def add_to_cart(self):
        arcade.draw_rectangle_outline(625, 50, 50, 50, arcade.color.WHITE)
        arcade.draw_text("ADD TO\nCART", 625, 50, arcade.color.WHITE, 9, 200,
                         "center", 'Arial', True, False, "center", "center")

    def ship_out(self):
        arcade.draw_rectangle_outline(550, 50, 50, 50, arcade.color.WHITE)
        arcade.draw_text("SHIP\nOUT", 550, 50, arcade.color.WHITE, 9, 200,
                         "center", 'Arial', True, False, "center", "center")

    def order_fulfillment(self):
        arcade.draw_rectangle_outline(475, 50, 50, 50, arcade.color.WHITE)
        arcade.draw_text("ORDER\nFULFILL\nMENT", 475, 50, arcade.color.WHITE, 9, 200,
                         "center", 'Arial', True, False, "center", "center")


def on_update(delta_time):
    global clicked_prev, clicked_next, clicked_shipment
    global clicked_order_fulfillment, clicked_ship_out, clicked_add_to_cart
    global item, carts, shelves, cart_number, shelf_number, product_numbers
    global bins, bin_number
    global cart1, cart2, cart3

    if clicked_prev:
        print("previous item")
        if item > 0:
            item -= 1
            afc.Item.shipment[item]
        print(item)
        print(afc.Item.shipment[item])
        clicked_prev = False

    if clicked_next:
        print("next item")
        if item < len(afc.Item.shipment) - 1:
            item += 1
            afc.Item.shipment[item]
        print(item)
        print(afc.Item.shipment[item])
        clicked_next = False

    if clicked_add_to_cart:
        print("Added to cart")
        if afc.Item.shipment[item].number in food_shelf.product_numbers:
            cart1.scan_onto_cart()
        elif afc.Item.shipment[item].number in tech_shelf.product_numbers:
            cart2.scan_onto_cart()
        elif afc.Item.shipment[item].number in footwear_shelf.product_numbers:
            cart3.scan_onto_cart()
        clicked_add_to_cart = False

    if clicked_shipment:
        print("shipment")
        for num in range(5):
            product_List = ["alan's left shoe", "iphone", "steak", "fish"]
            product = random.choice(product_List)
            if product == "alan's left shoe":
                new_item = afc.Item.alans_left_shoe()
            elif product == "iphone":
                new_item = afc.Item.iphone()
            elif product == "steak":
                new_item = afc.Item.steak()
            elif product == "fish":
                new_item = afc.Item.fish()

        clicked_shipment = False

    if clicked_order_fulfillment:
        print("Order Fulfillment Station")
        bins.append(afc.Bin())
        bins[bin_number].assign_order()
        bins[bin_number].scan_into_bin
        packages.append(afc.Package(
            bins[bin_number], "A test case", "A test case"))
        clicked_order_fulfillment = False

    if clicked_ship_out:
        print("Ship - Out Station")
        afc.Package.send_to_truck()
        clicked_ship_out = False


def on_draw():
    arcade.start_render()
    drawings.box_item(afc.Item.shipment[item], afc.Item.shipment[item].name,
                      afc.Item.shipment[item].dimensions)
    drawings.prev(afc.Item.shipment[item])
    drawings.next(afc.Item.shipment[item])
    drawings.shipment(afc.Item.shipment[item])
    drawings.add_to_cart(afc.Item.shipment[item])
    drawings.ship_out(afc.Item.shipment[item])
    drawings.order_fulfillment(afc.Item.shipment[item])


def on_key_press(key, modifiers):
    global clicked_prev, clicked_next, clicked_shipment

    if key == arcade.key.LEFT:
        clicked_prev = True

    if key == arcade.key.RIGHT:
        clicked_next = True

    if key == arcade.key.ENTER:
        clicked_shipment = True


def on_key_release(key, modifiers):
    global clicked_prev, clicked_next, clicked_shipment

    if key == arcade.key.LEFT:
        clicked_prev = False

    if key == arcade.key.RIGHT:
        clicked_next = False

    if key == arcade.key.ENTER:
        clicked_shipment = False


def on_mouse_press(x, y, button, modifiers):
    global clicked_prev, clicked_next, clicked_shipment
    global clicked_order_fulfillment, clicked_ship_out, clicked_add_to_cart

    # Previous button
    if (25 <= x <= 75) and (275 <= y <= 325):
        clicked_prev = True

    # Next button
    if (725 <= x <= 775) and (275 <= y <= 325):
        clicked_next = True

    # shipment button
    if (675 <= x <= 725) and (25 <= y <= 75):
        clicked_shipment = True

    # Previous cart button
    if (450 <= x <= 500) and (25 <= y <= 75):
        clicked_order_fulfillment = True

    # In cart button
    if (525 <= x <= 575) and (25 <= y <= 75):
        clicked_ship_out = True

    # Next cart button
    if (600 <= x <= 650) and (25 <= y <= 75):
        clicked_add_to_cart = True


def main():
    arcade.open_window(screen_width, screen_height,
                       "Amazon Fulfillment Centre")
    arcade.set_background_color(arcade.color.BLACK)

    arcade.schedule(on_update, 1/60)
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == "__main__":
    main()
