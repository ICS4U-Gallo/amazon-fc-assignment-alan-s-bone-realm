# from amazon_fc import *
import arcade

screen_width = 800
screen_height = 600


def on_draw(delta_time):
    arcade.start_render()
    pass


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(screen_width, screen_height, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press


def main():
    arcade.open_window(screen_width, screen_height, "Amazon FC")
    arcade.set_background_color(arcade.color.BLACK)

    # Call on_draw every 60th of a second
    arcade.schedule(on_draw, 1/60)
    window = arcade.get_window
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    

    arcade.run()

if __name__ == "__main__":
    main()