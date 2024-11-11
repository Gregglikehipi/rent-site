import sqlite3


class Database:
    def __init__(self, db_name="rent_site.db"):
        self.dbname = f"sqlite3:/{db_name}"
        self.conn = sqlite3.connect(db_name)
