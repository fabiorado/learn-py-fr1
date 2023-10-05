import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import MDList
from kivymd.uix.dialog import MDDialog
import sqlite3

# Initialize Kivy and KivyMD
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

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = MDTextField()
        self.password = MDTextField()
        self.login_button = MDRaisedButton(text='Login', on_release=self.login)
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.username)
        self.layout.add_widget(self.password)
        self.layout.add_widget(self.login_button)
        self.add_widget(self.layout)

    def login(self, instance):
        # Add login logic here
        pass

class UserManagementScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add user management UI and logic here
        pass

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add main screen UI and logic here
        pass

class MyApp(MDApp):
    def build(self):
        # Create the screen manager
        self.sm = ScreenManager()
        self.login_screen = LoginScreen(name='login')
        self.user_management_screen = UserManagementScreen(name='user_management')
        self.main_screen = MainScreen(name='main')
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.user_management_screen)
        self.sm.add_widget(self.main_screen)
        return self.sm

if __name__ == '__main__':
    MyApp().run()
