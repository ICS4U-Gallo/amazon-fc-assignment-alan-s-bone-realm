import amazon_fc as afc
import arcade

screen_width = 800
screen_height = 600


iphone = afc.Item("iphone", 100, "iphone.png", 10, 4, 1)
steak = afc.Item("Steak", 2, "steak.png", 100, 50, 5)
fish = afc.Item("Fish", 12415, "fish.png", 20, 10, 54)
shoe = afc.Item("Shoe", 13467, "shoe.png", 30, 5, 10)


clicked_prev = False
clicked_next = False
clicked_create = False

clicked_order_fulfillment = False
clicked_ship_out = False
clicked_add_to_cart = False


item = 0
cart_number = 0
carts = []


shelf_number = 0
shelves = []
product_numbers = []

bin_number = 0
bins = []

package_number = 0
packages = []


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

    def create(self):
        arcade.draw_rectangle_outline(725, 75, 100, 100, arcade.color.WHITE)
        arcade.draw_text("CREATE", 725, 75, arcade.color.WHITE, 15, 200,
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
    global clicked_prev, clicked_next, clicked_create
    global clicked_order_fulfillment, clicked_ship_out, clicked_add_to_cart
    global item, carts, shelves, cart_number, shelf_number, product_numbers
    global bins, bin_number

    if clicked_prev:
        print("previous item")
        if item > 0:
            item -= 1
            afc.Item.shipment[item]
        print(item)
        print(afc.Item.shipment[item])
        # print("Cart ID:", str(cart_id))
        clicked_prev = False

    if clicked_next:
        print("next item")
        if item < len(afc.Item.shipment) - 1:
            item += 1
            afc.Item.shipment[item]
        print(item)
        print(afc.Item.shipment[item])
        # print("Cart ID:", str(cart_id))
        clicked_next = False

    if clicked_add_to_cart:
        print("Added to cart")
        if afc.Item.shipment[item].number not in product_numbers:
            product_numbers.append(afc.Item.shipment[item].number)
        print(product_numbers)
        clicked_add_to_cart = False

    if clicked_create:
        print("create")
        shelves.append(afc.Shelf(shelf_number, afc.Item.shipment[item].number))
        carts.append(afc.Cart())
        carts[cart_number].assign_cart(carts[cart_number], shelves[shelf_number])
        carts[cart_number].scan_onto_cart(carts[cart_number])
        carts[cart_number].scan_onto_shelf(carts[cart_number])

        shelf_number += 1
        cart_number += 1

        clicked_create = False

    
    if clicked_order_fulfillment:
        print("Order Fulfillment Station")
        bins.append(afc.Bin())
        bins[bin_number].assign_order()
        bins[bin_number].scan_into_bin
        packages.append(afc.Package(bins[bin_number], "A test case", "A test case"))
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
    drawings.create(afc.Item.shipment[item])
    drawings.add_to_cart(afc.Item.shipment[item])
    drawings.ship_out(afc.Item.shipment[item])
    drawings.order_fulfillment(afc.Item.shipment[item])


def on_key_press(key, modifiers):
    global clicked_prev, clicked_next, clicked_create

    if key == arcade.key.LEFT:
        clicked_prev = True

    if key == arcade.key.RIGHT:
        clicked_next = True

    if key == arcade.key.ENTER:
        clicked_create = True


def on_key_release(key, modifiers):
    global clicked_prev, clicked_next, clicked_create

    if key == arcade.key.LEFT:
        clicked_prev = False

    if key == arcade.key.RIGHT:
        clicked_next = False

    if key == arcade.key.ENTER:
        clicked_create = False


def on_mouse_press(x, y, button, modifiers):
    global clicked_prev, clicked_next, clicked_create
    global clicked_order_fulfillment, clicked_ship_out, clicked_add_to_cart

    # Previous button
    if (25 <= x <= 75) and (275 <= y <= 325):
        clicked_prev = True

    # Next button
    if (725 <= x <= 775) and (275 <= y <= 325):
        clicked_next = True

    # Create button
    if (675 <= x <= 775) and (25 <= y <= 125):
        clicked_create = True

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
