import random
import string

DB_NAME = 'Wydawnictwo'

class Rola(object):
    TABLE = 'Rola'
    ROLES = ['Administrator', 'Redaktor', 'Recenzent', 'Kontrybutor', 'Uzytkownik']
    DISCRIPTIONS = ['Discription 1', 'Discription 2', 'Discription 3', 'Discription 4', 'Discription 5']

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

    def genSqlInsertRola(self, index):
        id = self.getMaxIntVal('Rola', 'idRola') + 1
        val = []
        sql = "INSERT INTO `Wydawnictwo`.`Rola` (`idRola`, `Nazwa`, `Opis`) VALUES (%s, %s, %s);"
        val.append(id)
        val.append(self.addQuotes(self.ROLES[index]))
        val.append(self.addQuotes(random.choice(self.DISCRIPTIONS)))
        sql = sql % tuple(val)
        return sql

    def insertRola(self):
        for i in range(len(self.ROLES)):
            self.cursor.execute(self.genSqlInsertRola(i))
            self.db.commit()

    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()

