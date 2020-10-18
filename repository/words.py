import mysql.connector


class conection:
    def __init__(self):
        self.myDb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database='words'
        )
        self.myCursor = self.myDb.cursor()


    def getAllWords(self):
        sql = "Select * from words"
        self.myCursor.execute(sql)
        self.result = self.myCursor.fetchall()

        return self.result






