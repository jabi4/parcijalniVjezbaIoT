import sqlite3

def initDB()
    DB = "IoT.db"
    connection = sqlite3.connect(DB)
    return connection