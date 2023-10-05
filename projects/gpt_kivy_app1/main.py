import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
import sqlite3

# Initialize Kivy
kivy.require('1.11.1')

# Database connection
conn = sqlite3.connect('app_db.db')
c = conn.cursor()

# Create tables if they don't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        name TEXT,
        notes TEXT
    )
''')
conn.commit()

class UserManager:
    def __init__(self):
        pass

    def create_user(self, username, password):
        try:
            conn = sqlite3.connect('app_db.db')
            cursor = conn.cursor()
            # Check if the username already exists
            cursor.execute("SELECT id FROM users WHERE username=?", (username,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                return "Username already exists."
            
            # Insert the new user into the database
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            return "User created successfully."

        except sqlite3.Error as e:
            return f"Error creating user: {e}"
        finally:
            conn.close()

    def authenticate_user(self, username, password):
        try:
            conn = sqlite3.connect('app_db.db')
            cursor = conn.cursor()
            
            # Check if the username and password match a user in the database
            cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
            user = cursor.fetchone()
            
            if user:
                return "Authentication successful."
            else:
                return "Authentication failed. Invalid username or password."

        except sqlite3.Error as e:
            return f"Error authenticating user: {e}"
        finally:
            conn.close()

    def get_users(self):
        try:
            conn = sqlite3.connect('app_db.db')
            cursor = conn.cursor()

            # Retrieve all users from the database
            cursor.execute("SELECT id, username FROM users")
            users = cursor.fetchall()
            return users

        except sqlite3.Error as e:
            return f"Error retrieving users: {e}"
        finally:
            conn.close()

    def update_user(self, user_id, new_password):
        # Add logic to update a user's password in the database
        pass

    def delete_user(self, user_id):
        try:
            conn = sqlite3.connect('app_db.db')
            cursor = conn.cursor()

            # Delete the user with the provided user_id
            cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
            conn.commit()
            return "User deleted successfully."

        except sqlite3.Error as e:
            return f"Error deleting user: {e}"
        finally:
            conn.close()

class ItemManager:
    def __init__(self):
        pass

    def create_item(self, name, notes):
        try:
            conn = sqlite3.connect('app_db.db')
            cursor = conn.cursor()
            
            # Insert the new item into the database
            cursor.execute("INSERT INTO items (name, notes) VALUES (?, ?)", (name, notes))
            conn.commit()
            return "Item created successfully."

        except sqlite3.Error as e:
            return f"Error creating item: {e}"
        finally:
            conn.close()

    def get_items(self):
        try:
            conn = sqlite3.connect('app_db.db')
            cursor = conn.cursor()

            # Retrieve all items from the database
            cursor.execute("SELECT id, name, notes FROM items")
            items = cursor.fetchall()
            return items

        except sqlite3.Error as e:
            return f"Error retrieving items: {e}"
        finally:
            conn.close()

    def update_item(self, item_id, new_name, new_notes):
        try:
            conn = sqlite3.connect('app_db.db')
            cursor = conn.cursor()

            # Update the item with the provided item_id
            cursor.execute("UPDATE items SET name=?, notes=? WHERE id=?", (new_name, new_notes, item_id))
            conn.commit()
            return "Item updated successfully."

        except sqlite3.Error as e:
            return f"Error updating item: {e}"
        finally:
            conn.close()

    def delete_item(self, item_id):
        try:
            conn = sqlite3.connect('app_db.db')
            cursor = conn.cursor()

            # Delete the item with the provided item_id
            cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
            conn.commit()
            return "Item deleted successfully."

        except sqlite3.Error as e:
            return f"Error deleting item: {e}"
        finally:
            conn.close()

    def refresh_items(self):
        # Fetch items from the ItemManager and update the RecycleView data
        items = self.item_manager.get_items()
        self.data = [{'text': f"Name: {item[1]}, Notes: {item[2]}", 'item_id': item[0]} for item in items]

class UserManagementPopup(Popup):
    def __init__(self, user_manager, **kwargs):
        super().__init__(**kwargs)
        self.user_manager = user_manager
        self.title = "User Management"
        self.layout = BoxLayout(orientation="vertical")
        self.username_input = TextInput(hint_text="Username")
        self.password_input = TextInput(hint_text="Password", password=True)
        self.create_user_button = Button(text="Create User")
        self.create_user_button.bind(on_release=self.create_user)
        self.layout.add_widget(self.username_input)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.create_user_button)
        self.content = self.layout

    def create_user(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        if username and password:
            self.user_manager.create_user(username, password)
            self.dismiss()

class ItemList(RecycleView):
    def __init__(self, item_manager, **kwargs):
        super().__init__(**kwargs)
        self.item_manager = item_manager
        self.data = []

class ItemListButton(RecycleDataViewBehavior, Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainScreen(BoxLayout):
    def __init__(self, user_manager, item_manager, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.user_manager = user_manager
        self.item_manager = item_manager
        self.login_label = Label(text="Welcome!")
        self.logout_button = Button(text="Logout", on_release=self.logout)
        self.add_user_button = Button(text="Add User", on_release=self.open_user_management)
        self.user_list = UserManager(user_manager)
        self.item_list = ItemList(item_manager)
        self.add_widget(self.login_label)
        self.add_widget(self.logout_button)
        self.add_widget(self.add_user_button)
        self.add_widget(self.item_list)
        self.add_widget(self.user_list)

    def open_user_management(self, instance):
        user_management_popup = UserManagementPopup(self.user_manager)
        user_management_popup.open()

    def logout(self, instance):
        # Add logout logic
        pass

class MyApp(App):
    def build(self):
        user_manager = UserManager()
        item_manager = ItemManager()
        return MainScreen(user_manager, item_manager)

if __name__ == '__main__':
    MyApp().run()
