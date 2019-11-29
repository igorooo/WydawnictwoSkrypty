import names
import random
import string

DB_NAME = 'Wydawnictwo'

class Przypisanie(object):
    TABLE = 'Przypisanie'


    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor
        self.review = self.convertToBinaryData()


    def getMaxIntVal(self, table, column):
        self.cursor.execute("SELECT MAX(" + column + ") FROM " + DB_NAME + '.' + table)
        result = self.cursor.fetchall()
        for i in result:
            if(i[0] == None):
                return 0
            maxIntVal = (int)(i[0])
        return maxIntVal

    def getRandomKontrybutor(self):
        n = self.getMaxIntVal('Uzytkownik', 'idUzytkownik')
        kontrybutorId = n
        if kontrybutorId == 0:
            raise Exception('There is 0 elements in table Uzytkownik!')
        self.cursor.execute("SELECT idUzytkownik FROM " + DB_NAME + '.Uzytkownik WHERE idUzytkownik='+ str(random.randint(1, n)))
        result = self.cursor.fetchall()
        for i in result:
            if (i[0] == None):
                return self.getRandomKontrybutor()
            kontrybutorId = (int)(i[0])
        return kontrybutorId

    def getRandomArtykul(self):
        n = self.getMaxIntVal('Artykul', 'idArtykul')
        artykulId = n
        wersja = 1
        if artykulId == 0:
            raise Exception('There is 0 elements in table Artykul!')
        self.cursor.execute("SELECT idArtykul FROM " + DB_NAME + '.Artykul WHERE idArtykul='+ str(random.randint(1, n)))
        result = self.cursor.fetchall()
        for i in result:
            if (i[0] == None):
                raise Exception("There is no Artykul in database!")
            artykulId = (int)(i[0])

        self.cursor.execute(
            "SELECT MAX(Wersja) FROM " + DB_NAME + '.Artykul WHERE idArtykul=' + str(artykulId))
        result = self.cursor.fetchall()
        for i in result:
            if (i[0] == None):
                raise Exception("There is no Artykul in database!")
            wersja = (int)(i[0])

        return (artykulId, wersja)


    def genSqlInsertPrzypisanie(self):
        sql = "INSERT INTO `Wydawnictwo`.`Przypisanie` (`Artykul_idArtykul`, `Artykul_Wersja`, `Kategoria_idKategoria`) VALUES (%s, %s, %s);"
        sql = "INSERT INTO `Wydawnictwo`.`Recenzja` (Recenzja, Artykul_idArtykul, Artykul_Wersja, Uzytkownik_idUzytkownik) VALUES (%s, %s, %s, %s);"

        kat = self.getRandomKat()
        article = self.getRandomArtykul()

        val = [article[0], article[1], rev]
        return (sql, tuple(val))

    def insertPrzypisanie(self, number):
        for i in range(number):
            sql = self.genSqlInsertRecenzja()
            self.cursor.execute(sql[0], sql[1])
            self.db.commit()


    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()
