import sqlite3
import uuid
from sqlite3 import Error
from pathlib import Path


def create_db_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file) # create in memory only
    except Error as e:
        print(e)

    return conn

def create_table(conn, script):
    try:
        c = conn.cursor()
        c.execute(script)
    except Error as e:
        print(e)

