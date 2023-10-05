import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3
from datetime import datetime

# Initialize Kivy and KivyMD
kivy.require('1.11.1')

KV = """
BoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Item Form"
        elevation: 10

    MDScreen:

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

"""

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

    def upsert_item(self):
        name = self.root.ids.name_field.text
        description = self.root.ids.description_field.text
        modified_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.root.ids.modified_date_field.text = modified_date

        # Check if the item already exists
        self.cursor.execute("SELECT * FROM items WHERE name=?", (name,))
        existing_item = self.cursor.fetchone()

        if existing_item:
            # Update the existing item
            self.cursor.execute(
                "UPDATE items SET description=?, modified_date=? WHERE name=?",
                (description, modified_date, name)
            )
        else:
            # Insert a new item
            self.cursor.execute(
                "INSERT INTO items (name, description, modified_date) VALUES (?, ?, ?)",
                (name, description, modified_date)
            )

        self.connection.commit()
        self.root.ids.name_field.text = ""
        self.root.ids.description_field.text = ""
        self.root.ids.modified_date_field.text = modified_date

    def on_stop(self):
        self.connection.close()

if __name__ == "__main__":
    ItemManagerApp().run()
