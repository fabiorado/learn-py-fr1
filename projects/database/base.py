import datetime
import time
import uuid
import sqlite3
import hashlib
from sqlite3 import Error
from pathlib import Path

DB_NAME = "AcupuApp.db"

def get_time() -> str:
    """Returns a string with the current date and time."""

    return datetime.datetime.fromtimestamp(
        time.mktime(datetime.datetime.now().timetuple())
    ).strftime("%d-%m-%Y %H:%M:%S")


class Base:
    def __init__(self) -> None:
        self.db_file_path = Path().joinpath("data", DB_NAME)
        self.conn = self.create_connection(self.db_file_path)
        self.cursor = self.conn.cursor()
        self.user_data = {}

        # with self.conn:
        self._initialize_database(self.conn)

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def execute_sql(self, conn, script):
        try:
            c = conn.cursor()
            c.execute(script)
            conn.commit()
        except Error as e:
            print(e)
    
    def execute_sql_files(self, conn, scripts_file_path):
        for script_name in scripts_file_path.iterdir():
            if script_name.match("**.sql"):
                print(script_name)
                with open(script_name, 'r') as f:
                    self.execute_sql(conn, f.read())

    def _initialize_database(self, conn):

        if self.get_tables() == []:
            print("Initializing the database...")
            # Create tables
            scripts_file_path = Path().joinpath("scripts", "tables")
            self.execute_sql_files(conn, scripts_file_path)
            # Execute scripts Post-Deploy
            scripts_file_path = Path().joinpath("scripts", "post_deploy")
            self.execute_sql_files(conn, scripts_file_path)

    def add_user_credentials(self, user_id: str, user: str, password: str) -> bool:
        try:
            pwd = hashlib.sha256(password.encode()).hexdigest()
            sql = f"UPDATE user SET ModifiedOn = DATETIME(), LogonName = ?, HashedPassword = ? WHERE UserID = ?"
            self.cursor.execute(sql, (user, pwd, user_id))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    def set_user(self, data: dict) -> bool:
        """
        Parse the dict and create the dinamic UPDATE
        """
        print(data)

    def set_user_data(self, key, value):
        self.user_data[key] = value

    def deactivate_user(self) -> bool:
        pass

    def check_if_user_admin(self) -> bool:
        pass

    def check_login(self, usr: str, pwd: str) -> bool:
        
        pwd = hashlib.sha256(pwd.encode()).hexdigest()       
        sql = "SELECT * FROM user WHERE IsPermittedToLogon = 1 AND LogonName = ? AND HashedPassword = ?"
        self.cursor.execute(sql, (usr, pwd))
        
        if self.cursor.fetchall():
            return True
        else:
            return False

    def get_user_id(self,search_value) -> str:
        # I need to improve this!!!
        sql = f"SELECT UserID FROM user WHERE FullName LIKE '%{search_value}%'"
        self.cursor.execute(sql)
        user_id = self.cursor.fetchall()[0][0]
        return str(user_id)
    
    def get_users(self) -> list[str]:
        users: list[str] = []
        for row in self.cursor.execute("SELECT FullName FROM user"):
            users.append(row[0])
        return users
    
    def get_tables(self) -> list[str]:
        tables: list[str] = []
        for row in self.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'"):
            tables.append(row[0])
        return tables

if __name__ == "__main__":
    print("##################################")
    b = Base()

    user_id = b.get_user_id("admin")
    b.add_user_credentials(user_id, "admin", "admin")

    u = input("User: ")
    p = input("Password: ")

    if b.check_login(u, p):
        print("Oh yeah!")
    else:
        print("Nope!")

    