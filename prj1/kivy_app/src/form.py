from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('formStyle.kv')

class MyLayout(Widget):
    results = []
    def checkbox_click(self, instance, value, text):
        if value == True:
            self.results.append(text)
            self.ids.lblOutput.text = str(text)
        else:
            self.results.remove(text)

    def submit(self, instance):
        self.results.append(self.ids.txtName.text)
        self.ids.lblOutput.text = str(self.results)
    
    def clear(self, instance):
        self.ids.lblOutput.text = ""


class FormApp(App):
    def build(self):
        Window.clearcolor = (140/255,140/255,140/255,1)
        return MyLayout()


if __name__ == "__main__":
    FormApp().run()
    