# Template for the "Main.py" file with Kivy

[README](../README.md)  

``` python
import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.widget import Widget

class MyLayout(Widget):
    pass

class Main(App):

    def build(self):
        return MyLayout()

if __name__ == '__main__':
    Main().run()
```