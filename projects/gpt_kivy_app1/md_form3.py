from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
import sqlite3
from datetime import datetime

KV = """
BoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Item Manager"
        elevation: 10

    MDScreenManager:
        id: screen_manager

        MDScreen:
            name: "item_form"
            
            BoxLayout:
                orientation: "vertical"
                padding: dp(16)

                MDTextField:
                    id: name_field
                    hint_text: "Name"
                    required: True
                    mode: "fill"

                MDTextField:
                    id: description_field
                    hint_text: "Description"
                    required: True
                    mode: "fill"

                MDTextField:
                    id: modified_date_field
                    hint_text: "Modified Date"
                    readonly: True
                    mode: "fill"

                MDRaisedButton:
                    text: "Save"
                    on_release: app.upsert_item()

        MDScreen:
            name: "item_list"
            
            BoxLayout:
                orientation: "vertical"
                padding: dp(16)

                RecycleView:
                    id: item_list_view
                    viewclass: "ItemListItem"

<ItemListItem>:
    orientation: "horizontal"
    spacing: dp(10)

    MDLabel:
        text: root.name
        size_hint_x: 0.4

    MDLabel:
        text: root.description
        size_hint_x: 0.4

    MDLabel:
        text: root.modified_date
        size_hint_x: 0.2

    MDRaisedButton:
        text: "Delete"
        on_release: app.delete_item(root.name)

    MDBottomNavigation:
        panel_color: app.theme_cls.primary_color
        orientation: "horizontal"

        MDBottomNavigationItem:
            name: "item_form"
            text: "Item Form"
            icon: "pencil"

        MDBottomNavigationItem:
            name: "item_list"
            text: "Item List"
            icon: "format-list-bulleted"
"""

class ItemListItem(BoxLayout):
    name = StringProperty()
    description = StringProperty()
    modified_date = StringProperty()

class ItemFormScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name_field = Builder.load_string('''
MDTextField:
    hint_text: "Name"
    required: True
    mode: "fill"
''')
        self.description_field = Builder.load_string('''
MDTextField:
    hint_text: "Description"
    required: True
    mode: "fill"
''')
        self.modified_date_field = Builder.load_string('''
MDTextField:
    hint_text: "Modified Date"
    readonly: True
    mode: "fill"
''')
        self.save_button = MDRaisedButton(text="Save")
        self.save_button.bind(on_release=self.upsert_item)

        self.add_widget(self.name_field)
        self.add_widget(self.description_field)
        self.add_widget(self.modified_date_field)
        self.add_widget(self.save_button)

    def upsert_item(self, *args):
        name = self.name_field.text
        description = self.description_field.text
        modified_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.modified_date_field.text = modified_date

        # Check if the item already exists
        app = MDApp.get_running_app()
        cursor = app.cursor
        cursor.execute("SELECT * FROM items WHERE name=?", (name,))
        existing_item = cursor.fetchone()

        if existing_item:
            # Update the existing item
            cursor.execute(
                "UPDATE items SET description=?, modified_date=? WHERE name=?",
                (description, modified_date, name)
            )
        else:
            # Insert a new item
            cursor.execute(
                "INSERT INTO items (name, description, modified_date) VALUES (?, ?, ?)",
                (name, description, modified_date)
            )

        app.connection.commit()
        self.name_field.text = ""
        self.description_field.text = ""
        self.modified_date_field.text = modified_date

class ItemListScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scrollview = ScrollView()
        self.item_list = self.create_item_list()
        self.scrollview.add_widget(self.item_list)
        self.add_widget(self.scrollview)

    def create_item_list(self):
        app = MDApp.get_running_app()
        cursor = app.cursor
        cursor.execute("SELECT * FROM items")
        items = cursor.fetchall()

        item_list = MDList()

        for item in items:
            item_name = item[1]
            item_description = item[2]
            item_modified_date = item[3]

            list_item = ThreeLineListItem(
                text=item_name,
                secondary_text=item_description,
                tertiary_text=item_modified_date
            )

            delete_button = MDRaisedButton(
                text="Delete",
                on_release=lambda x, item_name=item_name: self.delete_item(item_name)
            )
            list_item.add_widget(delete_button)
            item_list.add_widget(list_item)

        return item_list

    def delete_item(self, item_name):
        app = MDApp.get_running_app()
        cursor = app.cursor
        cursor.execute("DELETE FROM items WHERE name=?", (item_name,))
        app.connection.commit()
        self.scrollview.remove_widget(self.item_list)
        self.item_list = self.create_item_list()
        self.scrollview.add_widget(self.item_list)

class ItemManagerApp(MDApp):
    def build(self):
        self.title = "Item Manager"
        self.connection = sqlite3.connect("items.db")
        self.cursor = self.connection.cursor()
        self.create_table()
        return Builder.load_string(KV)

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            modified_date TEXT
        )''')
        self.connection.commit()

    def switch_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

    def load_item_list(self):
        self.cursor.execute("SELECT * FROM items")
        items = self.cursor.fetchall()
        item_list_view = self.root.ids.item_list_view
        item_data = [{"name": item[1], "description": item[2], "modified_date": item[3]} for item in items]
        item_list_view.data = [{"viewclass": "ItemListItem", "name": item["name"], "description": item["description"], "modified_date": item["modified_date"]} for item in item_data]

    def delete_item(self, name):
        self.cursor.execute("DELETE FROM items WHERE name=?", (name,))
        self.connection.commit()
        self.load_item_list()

    def on_stop(self):
        self.connection.close()

if __name__ == "__main__":
    ItemManagerApp().run()
