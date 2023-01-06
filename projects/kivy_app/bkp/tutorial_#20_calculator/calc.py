from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500, 700)
Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        prior = self.ids.calc_input.text

        if prior == "0":
            self.ids.calc_input.text = str(button)
        else:
            if button == "." and "." in prior:
                pass
            elif button == "<<":
                self.ids.calc_input.text = prior[:-1]
            else:
                self.ids.calc_input.text = f"{prior}{button}"
            
    def equals(self):
        prior = self.ids.calc_input.text
        answer = eval(prior)
        self.ids.calc_input.text = str(answer)
        

class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()
    