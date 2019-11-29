import names
import random
import string

DB_NAME = 'Wydawnictwo'

class Recenzja(object):
    TABLE = 'Recenzja'
    FILE = 'data/SampleReview.pdf'


    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor


    def getUzytkownikArr(self):
        self.cursor.execute("SELECT Uzytkownik_idUzytkownik FROM " + DB_NAME + ".Uprawnienia WHERE Rola_idRola=3")
        result = self.cursor.fetchall()
        return result


    def addQuotes(self, val):
        return "'" + str(val) + "'"


    def convertToBinaryData(self):
        with open(self.FILE, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def getMaxIntVal(self, table, column):
        self.cursor.execute("SELECT MAX(" + column + ") FROM " + DB_NAME + '.' + table)
        result = self.cursor.fetchall()
        for i in result:
            if(i[0] == None):
                return 0
            maxIntVal = (int)(i[0])
        return maxIntVal

    def getRandomKontrybutor(self):
        return (random.choice(self.reviewers))[0]

    def getArtykulArr(self):
        self.cursor.execute("SELECT idArtykul, Wersja FROM " + DB_NAME + ".Artykul")
        result = self.cursor.fetchall()
        return result


    def genSqlInsertRecenzja(self, article):
        sql = "INSERT INTO `Wydawnictwo`.`Recenzja` (Recenzja, Artykul_idArtykul, Artykul_Wersja, Uzytkownik_idUzytkownik) VALUES (%s, %s, %s, %s);"

        pdf = self.review
        rev = self.getRandomKontrybutor()

        num = len(self.getArtykulArr())

        val = [pdf, article[0], article[1], rev]
        return (sql, tuple(val))

    def insertRecenzja(self):
        self.articles = self.getArtykulArr()
        self.review = self.convertToBinaryData()
        self.reviewers = self.getUzytkownikArr()
        for article in self.articles:
            sql = self.genSqlInsertRecenzja(article)
            self.cursor.execute(sql[0], sql[1])
            self.db.commit()


    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()
