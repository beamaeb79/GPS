from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from specialbuttons import LabelButton, ImageButton
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from homemapview import HomeMapView
from homegpshelper import HomeGpsHelper

Window.size = (375, 750)

class HomeScreen(Screen):
    pass
class MainApp(MDApp):

    search_menu = None

    current_lat = 1.304833
    current_lon = 103.831833

    def on_start(self):
        # Initialize GPS
        HomeGpsHelper().run()
        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.primary_style = "Light"

    def change_screen(self, screen_name, direction='forward', mode=""):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager

        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name

        if screen_name == "home_screen":
            self.root.ids.titlename.title = "Sg Transport"

MainApp().run()
