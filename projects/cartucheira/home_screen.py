from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatIconButton

class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in range(5):
            new_button = MDFillRoundFlatIconButton(
                icon = "language-python",
                text = f"Test {i}",
                size_hint = (1, 1),
            )
            self.ids.grid_home.add_widget(new_button)