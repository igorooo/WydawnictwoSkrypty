import random
import string

DB_NAME = 'Wydawnictwo'

class Kategoria(object):
    TABLE = 'Kategoria'
    CATEGORY = ['Fizyka', 'Matematyka', 'Informatyka', 'Biologia', 'Medycyna', 'Prawo', 'Polityka', 'Ekonomia', 'Astronomia']

    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor


    def addQuotes(self, val):
        return "'" + str(val) + "'"

    def randomString(self, stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def getMaxIntVal(self, table, column):
        self.cursor.execute("SELECT MAX(" + column + ") FROM " + DB_NAME + '.' + table)
        result = self.cursor.fetchall()
        for i in result:
            if(i[0] == None):
                return 0
            maxIntVal = (int)(i[0])
        return maxIntVal

    def genSqlInsertKategoria(self, index):
        id = self.getMaxIntVal(self.TABLE, 'idKategoria') + 1
        val = []
        sql = "INSERT INTO `Wydawnictwo`.`Kategoria` (`idKategoria`, `Nazwa`, `Opis`) VALUES (%s, %s, %s);"
        val.append(id)
        val.append(self.addQuotes(self.CATEGORY[index]))
        val.append(self.addQuotes(self.randomString(120)))
        sql = sql % tuple(val)
        return sql

    def insertKategoria(self):
        for i in range(len(self.CATEGORY)):
            self.cursor.execute(self.genSqlInsertKategoria(i))
            self.db.commit()

    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()

