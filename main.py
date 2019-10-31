import amazon_fc as afc
import arcade

screen_width = 800
screen_height = 600
iphone = afc.Item("iphone", 100, "iphone.png", 10, 4, 1)
steak = afc.Item("Steak", 2, "steak.png", 100, 50, 5)
fish = afc.Item("Fish", 12415, "fish.png", 20, 10, 54)
shoe = afc.Item("Shoe", 1342135, "shoe.png", 30, 5, 10)

shipment = [iphone, steak, fish, shoe]


current_screen = 0

clicked_prev = False
clicked_next = False
clicked_truck = False
clicked_cart = False
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
        arcade.draw_text(f"{self.dimensions[0]} cm x {self.dimensions[1]} cm x {self.dimensions[2]} cm",
                         400, 225, arcade.color.WHITE, 10, 200, "center", 'Arial',
                         True, False, "center", "center")

    def cart(self):
        arcade.draw_rectangle_outline(675, 50, 50, 50, arcade.color.WHITE)
        arcade.draw_text("CART", 675, 50, arcade.color.WHITE, 9,
                         200, "center", 'Arial', True, False, "center", "center")

    def truck(self):
        arcade.draw_rectangle_outline(750, 50, 50, 50, arcade.color.WHITE)
        arcade.draw_text("TRUCK", 750, 50, arcade.color.WHITE, 9,
                         200, "center", 'Arial', True, False, "center", "center")


def on_update(delta_time):
    global clicked_prev, clicked_next, clicked_truck, clicked_cart, shipment
    global item
    shelf = 0
    if clicked_prev:
        if item > 0:
            item -= 1
            shipment[item]
        print(item)
        print(shipment[item])
        clicked_prev = False

    if clicked_next:
        if item < len(shipment) - 1:
            item += 1
            shipment[item]
        print(item)
        print(shipment[item])
        clicked_next = False

    if clicked_truck:
        print("truck")
        clicked_truck = False
        # New cart and trollys and bins add in when tests are done

    if clicked_cart:
        print("cart")
        afc.Cart.assign_cart(shipment, shelf)
        for i in shipment:
            afc.Cart.scan_onto_cart(shipment, shipment[i])
        shelf += 1
        clicked_cart = False


def on_draw():
    arcade.start_render()
    drawings.box_item(
        shipment[item], shipment[item].name, shipment[item].dimensions)
    drawings.prev(shipment[item])
    drawings.next(shipment[item])
    drawings.truck(shipment[item])
    drawings.cart(shipment[item])


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global clicked_prev, clicked_next, clicked_truck, clicked_cart

    # Previous button
    if (25 <= x <= 75) and (275 <= y <= 325):
        clicked_prev = True

    # Next button
    if (725 <= x <= 775) and (275 <= y <= 325):
        clicked_next = True

    # Truck button
    if (725 <= x <= 775) and (25 <= y <= 75):
        clicked_truck = True

    # Cart button
    if (650 <= x <= 700) and (25 <= y <= 75):
        clicked_cart = True


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
