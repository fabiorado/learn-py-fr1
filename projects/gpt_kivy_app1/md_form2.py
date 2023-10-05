from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineListItem
from kivy.uix.scrollview import ScrollView
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

        ItemFormScreen:
            name: "item_form"

        ItemListScreen:
            name: "item_list"
"""

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

        item_list = MDList() ## ERROR !!!

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

        self.screen_manager = Builder.load_string(KV)
        return self.screen_manager

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            modified_date TEXT
        )''')
        self.connection.commit()

    def on_stop(self):
        self.connection.close()

if __name__ == "__main__":
    ItemManagerApp().run()
