import sqlite3

from contextlib import contextmanager

@contextmanager
def data_connection():
    connection = sqlite3.connect("app.db")
    connection.row_factory = sqlite3.Row
    
    try:
        yield connection
    finally:
        connection.close()


    