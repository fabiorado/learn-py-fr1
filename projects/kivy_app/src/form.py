from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('formStyle.kv')

class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.lblOutput.text = f'You selected "{value}"'
    
    def submit(self, instance):
        # self.results.append(self.ids.txtName.text)
        self.ids.lblOutput.text = f"Ok, thanks."
    
    def clear(self, instance):
        self.ids.lblOutput.text = ""


class FormApp(App):
    def build(self):
        Window.clearcolor = (140/255,140/255,140/255,1)
        return MyLayout()


if __name__ == "__main__":
    FormApp().run()
    