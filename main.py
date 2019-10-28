import amazon_fc as afc
import arcade

screen_width = 800
screen_height = 600
iphone = afc.Item("iphone", 100, 200, "iphone.png")

clicked_prev = False
clicked_next = False
item = 0

class drawings:
    def __init__(self, item_text: str):
        self.item_text = text
    
    def prev(self):
        arcade.draw_rectangle_outline(50, 300, 50, 50, arcade.color.WHITE)
        arcade.draw_text("PREV", 50, 300, arcade.color.WHITE, 10, 200, "center", 'Arial', True, False, "center", "center")
    
    def next(self):
        arcade.draw_rectangle_outline(750, 300, 50, 50, arcade.color.WHITE)
        arcade.draw_text("NEXT", 750, 300, arcade.color.WHITE, 10, 200, "center", 'Arial', True, False, "center", "center")

    def box_item(self, text):
        arcade.draw_rectangle_outline(400, 300, 200, 200, arcade.color.WHITE)
        arcade.draw_text(text, 400, 300, arcade.color.WHITE, 20, 200, "center", 'Arial', True, False, "center", "center")


def on_update(delta_time):
    global clicked_prev, clicked_next
    global item
    if clicked_prev:
        item -= 1
        print(item)
        clicked_prev = False

    if clicked_next:
        item += 1
        print(item)
        clicked_next = False


def on_draw():
    arcade.start_render()
    # Draw in here...
    drawings.box_item(iphone, iphone.name)
    drawings.prev(iphone)
    drawings.next(iphone)


def on_key_press(key, modifiers):
    global clicked_prev, clicked_next
    if key == arcade.key.A:
        clicked_prev = True
    
    if key == arcade.key.D:
        clicked_next = True


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global clicked_prev, clicked_next
    if (25 <= x <= 75) and (275 <= y <= 325):
        clicked_prev = True
    if (725 <= x <= 775) and (275 <= y <= 325):
        clicked_next = True

def setup():
    arcade.open_window(screen_width, screen_height, "Amazon Fulfillment Centre")
    arcade.set_background_color(arcade.color.BLACK)


    arcade.schedule(on_update, 1/60)
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()



if __name__ == "__main__":
    main()