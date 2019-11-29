import names
import random
import string

DB_NAME = 'Wydawnictwo'

class Weryfikanci(object):
    TABLE = 'Weryfikanci'


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

    def getGrupaWeryfikacjiArr(self):
        self.cursor.execute("SELECT idGrupaWeryfikacji FROM " + DB_NAME + ".GrupaWeryfikacji")
        result = self.cursor.fetchall()
        return result

    def getUzytkownikArr(self):
        self.cursor.execute("SELECT Uzytkownik_idUzytkownik FROM " + DB_NAME + ".Uprawnienia WHERE Rola_idRola=3")
        result = self.cursor.fetchall()
        return result


    def genSqlWeryfikanci(self, grupaW):
        sql = "INSERT INTO `Wydawnictwo`.`Weryfikanci` (`Uzytkownik_idUzytkownik`, `GrupaWeryfikacji_idGrupaWeryfikacji`) VALUES (%s, %s);"
        sqlArr = []
        id = grupaW[0]
        weryfi = self.getUzytkownikArr()
        maxU = len(weryfi)
        veryfiArr = []
        maxU = random.randint(1, maxU)
        for i in range(maxU):
            u = random.choice(weryfi)
            veryfiArr.append(u[0])
            weryfi.remove(u)

        for user in veryfiArr:
            val = (user, id)
            sqlArr.append(sql % val)
        return sqlArr

    def insertWeryfikanci(self):
        grupy = self.getGrupaWeryfikacjiArr()
        for grupa in grupy:
            sqlArr = self.genSqlWeryfikanci(grupa)
            for sql in sqlArr:
                self.cursor.execute(sql)
                self.db.commit()


    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()
