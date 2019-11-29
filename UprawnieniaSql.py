import random

DB_NAME = 'Wydawnictwo'

class Uprawnienia(object):
    TABLE = 'Uprawnienia'

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


    def genSqlInsertUprawnienia(self, idUzytkownik):
        maxIdRole = self.getMaxIntVal('Rola', 'idRola')
        sql = "INSERT INTO `Wydawnictwo`.`Uprawnienia` (`Rola_idRola`, `Uzytkownik_idUzytkownik`) VALUES (%s, %s);"

        val = [random.randint(1, maxIdRole), idUzytkownik]
        return sql % tuple(val)

    def insertUprawnienia(self):
        max = self.getMaxIntVal('Uzytkownik', 'idUzytkownik')
        for i in range(1, max):
            sql = self.genSqlInsertUprawnienia(i)
            self.cursor.execute(sql)
            self.db.commit()


    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()
