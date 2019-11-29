import names
import random
import string

DB_NAME = 'Wydawnictwo'

class Autorstwo(object):
    TABLE = 'Autorstwo'


    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor
        self.authors = self.getAutorArr()


    def getAutorArr(self):
        self.cursor.execute("SELECT idAutor FROM " + DB_NAME + ".Autor")
        result = self.cursor.fetchall()
        return result

    def getArtykulArr(self):
        self.cursor.execute("SELECT idArtykul, Wersja FROM " + DB_NAME + ".Artykul")
        result = self.cursor.fetchall()
        return result


    def genSqlAutorstwo(self):
        sql = "INSERT INTO `Wydawnictwo`.`Autorstwo` (`Autor_idAutor`, `Artykul_idArtykul`, `Artykul_Wersja`) VALUES (%s, %s, %s);"
        article = random.choice(self.articles)
        val = (random.choice(self.authors)[0], article[0], article[1])
        return (sql % val)

    def insertAutorstwo(self, number):
        self.articles = self.getArtykulArr()
        for i in range(number):
            sql = self.genSqlAutorstwo()
            self.cursor.execute(sql)
            self.db.commit()


    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()
