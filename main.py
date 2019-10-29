import amazon_fc as afc
import arcade

screen_width = 800
screen_height = 600
iphone = afc.Item("iphone", 100, 200, "iphone.png", 10, 4, 1)

current_screen = 0

clicked_prev = False
clicked_next = False
truck = False
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

    def truck(self):
        arcade.draw_rectangle_outline(750, 50, 50, 50, arcade.color.WHITE)
        arcade.draw_text("TRUCK", 750, 50, arcade.color.WHITE, 9, 
                         200, "center", 'Arial', True, False, "center", "center")


def on_update(delta_time):
    global clicked_prev, clicked_next, truck
    global item
    if clicked_prev:
        if item > 0:
            item -= 1
        print(item)
        clicked_prev = False

    if clicked_next:
        item += 1
        print(item)
        clicked_next = False
    
    if truck:
        print("truck")
        truck = False
        # New cart and trollys and bins add in when tests are done


def on_draw():
    arcade.start_render()
    drawings.box_item(iphone, iphone.name, iphone.dimensions)
    drawings.prev(iphone)
    drawings.next(iphone)
    drawings.truck(iphone)


def on_key_press(key, modifiers):
    global clicked_prev, clicked_next, truck
    if key == arcade.key.A:
        clicked_prev = True

    if key == arcade.key.D:
        clicked_next = True
    
    if key == arcade.key.T:
        truck = True


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global clicked_prev, clicked_next, truck
    if (25 <= x <= 75) and (275 <= y <= 325):
        clicked_prev = True
    if (725 <= x <= 775) and (275 <= y <= 325):
        clicked_next = True
    
    if (725 <= x <= 775) and (25 <= y <= 75):
        truck = True


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
