import pyglet
import divineoasis.components.button
import divineoasis.components.music_panel
import divineoasis.gui_manager

window = pyglet.window.Window(1280, 720)
gui = divineoasis.gui_manager.GuiManager(window)

red_button_image = pyglet.image.load("divineoasis/assets/user_interface/button_red_large.png")
red_button = divineoasis.components.button.Button("red_button", 10, (window.height - 74), 256, 64, red_button_image, "Red Button")

green_button_image = pyglet.image.load("divineoasis/assets/user_interface/button_green_large.png")
green_button = divineoasis.components.button.Button("green_button", 10, (window.height - 148), 256, 64, green_button_image, "Green Button")

blue_button_image = pyglet.image.load("divineoasis/assets/user_interface/button_blue_large.png")
blue_button = divineoasis.components.button.Button("blue_button", 10, (window.height - 222), 256, 64, blue_button_image, "Blue Button")

music_panel_image = pyglet.image.load("divineoasis/assets/user_interface/music_panel.png")
music_panel = divineoasis.components.music_panel.MusicPanel("music_panel", 10, (window.height - 330), 256, 98, music_panel_image, "Song Name", "Song Artist")

gui.add_component(red_button)
gui.add_component(green_button)
gui.add_component(blue_button)
gui.add_component(music_panel)

@window.event
def on_draw():
    window.clear()
    gui.update(0.0)

pyglet.app.run()
