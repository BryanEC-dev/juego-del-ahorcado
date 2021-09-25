import mysql.connector
from config.configuration import config


class conection:
    def __init__(self):
        self.myDb = mysql.connector.connect(
            host=config.get('DB','HOST'),
            user=config.get('DB','USER'),
            password=config.get('DB','PASSWORD'),
            database=config.get('DB','DATABASE')
        )
        self.myCursor = self.myDb.cursor()


    def getAllWords(self):
        sql = "Select * from words"
        self.myCursor.execute(sql)
        self.result = self.myCursor.fetchall()

        return self.result

    
    def insert_score(self, name, score):
        sql = "INSERT INTO points(first_name, score) VALUES (%s, %s)"
        val = (name,score)
        self.myCursor.execute(sql, val)
        
        self.myDb.commit()
        
        return self.myCursor.rowcount
    
    def get_score(self):
        sql = "Select * from points"
        self.myCursor.execute(sql)
        self.result = self.myCursor.fetchall()

        return self.result