import sqlite3
import uuid
from sqlite3 import Error
from pathlib import Path

VALID_TO = '9999-12-31 00:00:00'

# It will be transfered to another file (.sql)
TABLE_USER = """
CREATE TABLE IF NOT EXISTS user (
	UserID              varchar(50) NULL,
	FullName            text NULL,
    PreferredName       varchar(255) NULL,
    LogonName           varchar(255) NULL,
    HashedPassword      text NULL,
	EmailAddress        varchar(255) NULL,
	PhoneNumber         varchar(50) NULL,
    CustomFields        text NULL, -- JSON with the content of the "Other" fields
    UserPreferences     text NULL, -- JSON with interface preferences

    -- Control
	IsPermittedToLogon  boolean NOT NULL DEFAULT 1,
    IsUserAdmin         boolean NOT NULL DEFAULT 0,
	CreatedByID         varchar(50) NULL,
	CreatedOn           timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	ModifiedByID        varchar(50) NULL,
	ModifiedOn          timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- SCD2 
    IsCurrent           boolean NOT NULL DEFAULT 1,
    IsDeleted           boolean NOT NULL DEFAULT 0,
    ValidFrom           timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ValidTo             timestamp NOT NULL DEFAULT '9999-12-31 00:00:00'
);
"""

def create_conn(db_file):
    conn = None
    try:
        #conn = sqlite3.connect(':memory:') # create in memory only
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

def get_userid_by_name(conn, user_name):
    sql = f"""
        SELECT UserID 
        FROM user 
        WHERE IsCurrent = 1 
            AND FullName LIKE '%{user_name}%';
    """

    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    if rows == []:
        return None
    else:
        return rows[0][0]


def get_user_logon_permission(conn, userId):
    sql = 'SELECT IsPermittedToLogon FROM user WHERE IsCurrent = 1 AND UserID = ?'
    
    cur = conn.cursor()
    cur.execute(sql, (userId,))
    rows = cur.fetchall()

    if rows == []:
        return None
    elif rows[0][0] == 1:
        return True
    else:
        return False


def show_all_users(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE IsCurrent = 1")
    rows = cur.fetchall()

    for row in rows:
        print(row)


def add_user(conn, values):
    newGUID = str(uuid.uuid4())

    sql = f'''
        INSERT INTO user (UserID, FullName, EmailAddress, PhoneNumber)
        VALUES ("{newGUID}", ?, ?, ?)
    '''

    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    return newGUID


def block_user(conn, userId):
    sql = f'''
    UPDATE user
        SET IsPermittedToLogon = 0,
        ModifiedOn = DATETIME()
        WHERE UserID = ?
    '''
    cur = conn.cursor()
    cur.execute(sql, (userId,))
    conn.commit()


def main():

    # Runs in memory
    # db = ":memory:"
    # Create a database file
    db = Path("myapp.db")

    # # To use scripts
    # with open(Path('./sql/User.sql'), 'r') as script:
    #     sql_create_user_table = script.read()
    sql_create_user_table = TABLE_USER
    
    conn = create_conn(db)

    with conn:
        if 1==1: # validate if its the first execution
            create_table(conn, sql_create_user_table)

        # Get user status
        user_id = get_userid_by_name(conn, "Fabio Rado")
        user_status = get_user_logon_permission(conn, user_id)
        
        # Add User
        if user_status is None:
            user = ("Fabio Rado", "fabio.rado@gmail.com", "(418) 262-0723")
            user_id = add_user(conn, user)
            print("User created with de ID: ", user_id)
        else:
            print("User already exists. Status: ", user_status)

        # Update User (change status)
        if get_user_logon_permission(conn, user_id) is not None:
            block_user(conn, user_id)

        # Show all users
        show_all_users(conn)

if __name__ == "__main__":
    main()

