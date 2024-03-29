import names
import random
import string

DB_NAME = 'Wydawnictwo'

class Przypisanie(object):
    TABLE = 'Przypisanie'


    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor

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

    def getMaxWersja(self, id):
        wersja = 1
        self.cursor.execute(
            "SELECT MAX(Wersja) FROM " + DB_NAME + '.Artykul WHERE idArtykul=' + str(id))
        result = self.cursor.fetchall()
        for i in result:
            if (i[0] == None):
                return 1
            wersja = (int)(i[0])

        return wersja


    def genSqlInsertPrzypisanie(self, article):
        sql = "INSERT INTO `Wydawnictwo`.`Przypisanie` (`Artykul_idArtykul`, `Artykul_Wersja`, `Kategoria_idKategoria`) VALUES (%s, %s, %s);"
        sqlArr = []
        maxKat = self.getMaxIntVal("Kategoria", "idKategoria")

        kat = random.randint(1, maxKat)
        maxWersja = self.getMaxWersja(article)

        for i in range(1, maxWersja):
            val = [article, i, kat]
            sqlArr.append(sql % tuple(val))

        return sqlArr

    def insertPrzypisanie(self):
        max = self.getMaxIntVal("Artykul", "idArtykul")
        for i in range(max):
            sqlArr = self.genSqlInsertPrzypisanie(i)
            for sql in sqlArr:
                self.cursor.execute(sql)
                self.db.commit()


    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()
