import sqlite3 


"""
Question:
QuestionID: Primary Key, QuestionText: str, Answer1: str,Answer2: str,Answer3: str,Answer4: str, RightAnwer: str, Subject: int: 

"""

class DataBase:

    def  __init__(self, dbName):
        self.dbName = dbName

    def connect(self):
        self.conn =  sqlite3.connect(self.dbName)
        self.cursor = self.conn.commit()

    def disconnect(self):
        self.conn.close()

    def create(self):
        self.connect()
        sql = """CREATE TABLE Question (
                        QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
                        QuestionText TEXT NOT NULL,
                        Answer1 TEXT NOT NULL,
                        Answer2 TEXT NOT NULL,
                        Answer3 TEXT NOT NULL,
                        Answer4 TEXT NOT NULL,
                        RightAnswer TEXT NOT NULL,
                        Subject INTEGER NOT NULL
                        );"""

        self.cursor.execute(sql)

        self.disconnect()

        