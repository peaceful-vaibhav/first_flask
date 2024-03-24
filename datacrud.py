# This function is built to perform the essential steps required for the
# interaction with the SQLite DB

import sqlite3
import os
from datetime import datetime, timezone

def insert_data(filename, blob_data):
    check_flag = ""
    if os.path.isfile("test.db"):
        sqlite_connection = sqlite3.connect('test.db')
        cursor = sqlite_connection.cursor()
        print("Connected to SQLite")
        query = """ INSERT INTO test_schema (name, date_added, image_file) VALUES (?, ?, ?) """
        data_tuple = (filename, datetime.now(timezone.utc), blob_data)
        cursor.execute(query, data_tuple)
        check_flag = "inserted"
        print(f"{type(sqlite_connection)}, value is: {sqlite_connection}")
    else:
        sqlite_connection = sqlite3.connect('test.db')
        cursor = sqlite_connection.cursor()
        query = """ CREATE TABLE test_schema (name TEXT, date_added DATETIME PRIMARY KEY, image_file BLOB NOT NULL) """
        cursor.execute(query)
        check_flag = "created"
        print(f"{type(sqlite_connection)}, value is: {sqlite_connection}")

    sqlite_connection.commit()
    cursor.close()
    return check_flag

def fetch_data(filename):
    sqlite_connection = sqlite3.connect('test.db')
    cursor = sqlite_connection.cursor()
    query = """SELECT name, date_added from test_schema """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    sqlite_connection.commit()
    cursor.close()
