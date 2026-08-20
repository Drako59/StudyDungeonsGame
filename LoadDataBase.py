import sqlite3
from DataBase import DataBase



def main():

    db = DataBase("questionDb.db")
    db.create()



if __name__ == '__main__':
    main()