from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from home_screen import HomeScreen


Window.size = (900, 500)

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        self.screen_manager = ScreenManager()

    def build(self) -> ScreenManager:

        # Theme
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"
        self.title = "Cartucheira"

        # Add the screens here
        screens = [
            HomeScreen(name='home')
            # , ExecPyScript(name='exec_py')
        ]

        for screen in screens:
            self.screen_manager.add_widget(screen)

        return self.screen_manager
    

if __name__ == "__main__":
    MainApp().run()
