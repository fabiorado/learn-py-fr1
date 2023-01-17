import sqlite3
import hashlib

def init():
    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id integer PRIMARY KEY ASC,
        username varchar(255) not null,
        password varchar(255) not null
    )
    """)

    usr1, pwd1 = "mike", hashlib.sha256("mike123".encode()).hexdigest()
    usr2, pwd2 = "john", hashlib.sha256("john123".encode()).hexdigest()
    usr3, pwd3 = "strike", hashlib.sha256("strike123".encode()).hexdigest()
    usr4, pwd4 = "neuro", hashlib.sha256("neuro123".encode()).hexdigest()

    sql = "INSERT INTO user (username, password) VALUES (?, ?)"
    cur.execute(sql, (usr1, pwd1))
    conn.commit()
    cur.execute(sql, (usr2, pwd2))
    conn.commit()
    cur.execute(sql, (usr3, pwd3))
    conn.commit()
    cur.execute(sql, (usr4, pwd4))
    conn.commit()

    return cur


def check_login(usr, pwd: str):

    cur = init()

    pwd = hashlib.sha256(pwd.encode()).hexdigest()

    sql = "SELECT * FROM user WHERE username = ? AND password = ?"
    cur.execute(sql, (usr, pwd))

    if cur.fetchall():
        print("Oh yeah!")
    else:
        print("Nope!")

if __name__ == "__main__":
    u = input("User: ")
    p = input("Password: ")
    check_login(u, p)

