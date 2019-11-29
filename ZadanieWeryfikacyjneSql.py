import names
import random
import string

DB_NAME = 'Wydawnictwo'

class ZadanieWeryfikacyjne(object):
    TABLE = 'ZadanieWeryfikacyjne'
    DOMAIN = ['Weryfikacja techniczna', 'Weryfikacja merytoryczna', 'Weryfikacja formy', 'Weryfikacja referencji']
    RESULT = ['Pozytywny', 'Negatywny']


    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor

    def addQuotes(self, val):
        return "'" + str(val) + "'"


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

    def getArtykulArr(self):
        n = self.getMaxIntVal('Artykul', 'idArtykul')
        artykulId = n
        wersja = 1
        if artykulId == 0:
            raise Exception('There is 0 elements in table Artykul!')
        self.cursor.execute("SELECT idArtykul, Wersja FROM " + DB_NAME + ".Artykul WHERE Etap='Weryfikacja'")
        result = self.cursor.fetchall()
        return result


    def genSqlInsertZadanieWeryfikacyjneself(self, article):
        sql = "INSERT INTO `Wydawnictwo`.`ZadanieWeryfikacyjne` (`idZadanieWeryfikacyjne`, `Zakres`, `Wynik`, `Artykul_idArtykul`, `Artykul_Wersja`, `GrupaWeryfikacji_idGrupaWeryfikacji`) VALUES (%s, %s, %s, %s, %s, %s);"

        id = self.getMaxIntVal("ZadanieWeryfikacyjne", "idZadanieWeryfikacyjne") + 1
        zakres = random.choice(self.DOMAIN)
        wynik = self.addQuotes(random.choice(self.RESULT))
        idArtykul = article[0]
        wersja = article[1]
        gr = random.randint(1 ,self.getMaxIntVal("GrupaWeryfikacji", "idGrupaWeryfikacji"))
        val = (id, self.addQuotes(zakres), wynik, idArtykul, wersja, gr)
        sql = sql % val
        return sql

    def insertZadanieWeryfikacyjne(self):
        articles = self.getArtykulArr()
        for article in articles:
            sql = self.genSqlInsertZadanieWeryfikacyjneself(article)
            self.cursor.execute(sql)
            self.db.commit()


    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()
