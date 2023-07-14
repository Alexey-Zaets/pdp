import sqlite3


class DBConnection:

    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def __enter__(self):
        if not self.connection:
            self.connection = sqlite3.connect(self.db_file)
        return self. connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
