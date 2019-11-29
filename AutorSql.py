import names
import random
import string

DB_NAME = 'seba'

class Autor(object):
    TABLE = 'Autor'
    DEGREE = ['B.Sc', 'M.Sc', 'Ph.D', 'Prof']
    BIOGRAPHY = ['BIOGRAFIA NUMER 1', 'BIOGRAFIA NUMER 2', 'BIOGRAFIA NUMER 3', 'BIOGRAFIA NUMER 4', 'BIOGRAFIA NUMER 5']

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

    def genSqlInsertAutor(self):
        id = self.getMaxIntVal(self.TABLE, 'idAutor') + 1
        val = []
        sql = "INSERT INTO `seba`.`Autor` (`idAutor`, `Nazwisko`, `Imie`, `Stopień`, `Biografia`) VALUES (%s, %s, %s, %s, %s)";
        name = names.get_first_name()
        surname = names.get_last_name()
        val.append(id)
        val.append(self.addQuotes(surname))
        val.append(self.addQuotes(name))
        val.append(self.addQuotes(random.choice(self.DEGREE)))
        val.append(self.addQuotes(random.choice(self.BIOGRAPHY)))
        sql = sql % tuple(val)
        return sql

    def insertAutor(self, number):
        for i in range(number):
            self.cursor.execute(self.genSqlInsertAutor())
            self.db.commit()

    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()

