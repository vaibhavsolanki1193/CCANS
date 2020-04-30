import sqlite3
from sqlite3 import Error


class dbFunctions():
    def __init__(self):
        self.con = sqlite3.connect(r"data/UCCANS_DB.sqlite")
        self.cur = self.con.cursor()

    def insert_test(self):
        sql_insert = """
                    INSERT INTO test(first, second) VALUES (7,8)"""

        self.cur.execute(sql_insert)
        self.con.commit()

    def show_table(self):
        for row in self.cur.execute('SELECT * from test'):
            print(row[1])

    def __del__(self):
        self.con.close()

dbObject = dbFunctions()
# dbObject.insert_test()
dbObject.show_table()
