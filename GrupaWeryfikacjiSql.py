import random
import string

DB_NAME = 'Wydawnictwo'

class GrupaWeryfikacji(object):
    TABLE = 'GrupaWeryfikacji'

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

    def genSqlInsertGrupaWeryfikacji(self):
        id = self.getMaxIntVal(self.TABLE, 'idGrupaWeryfikacji') + 1
        val = []
        sql = "INSERT INTO `Wydawnictwo`.`GrupaWeryfikacji` (`idGrupaWeryfikacji`, `Nazwa`) VALUES (%s, %s);"
        val.append(id)
        val.append(self.addQuotes("Grupa weryfikacji #" + str(id)))
        sql = sql % tuple(val)
        return sql

    def insertGrupaWeryfikacji(self, number):
        for i in range(number):
            self.cursor.execute(self.genSqlInsertGrupaWeryfikacji())
            self.db.commit()

    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()

