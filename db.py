import sqlite3


class Database:
    def __init__(self, db_name="university.db"):
        self.dbname = f"sqlite3:/{db_name}"
        self.conn = sqlite3.connect(db_name)



