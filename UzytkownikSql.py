import names
import random
import string

DB_NAME = 'Wydawnictwo'

class Uzytkownik(object):
    EMAIL_PROVIDERS = ['@gmail.com', '@yahoo.com', '@outlook.com', '@op.pl', '@hotmail.com', '@o2.pl'];
    TABLE = 'Uzytkownik'

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
            if (i[0] == None):
                return 0
            maxIntVal = (int)(i[0])
        return maxIntVal

    def genSqlInsertUzytkownik(self):
        id = self.getMaxIntVal(self.TABLE, 'idUzytkownik') + 1
        val = []
        sql = "INSERT INTO `Wydawnictwo`.`Uzytkownik` (`idUzytkownik`, `Nazwa`, `Login`, `Haslo`, `Email`) VALUES (%s, %s, %s, %s, %s)"
        name = names.get_first_name()
        surname = names.get_last_name()
        val.append(id)
        val.append(self.addQuotes(name + ' ' + surname))
        val.append(self.addQuotes(self.randomString(10)))
        val.append(self.addQuotes(self.randomString(10)))
        val.append(self.addQuotes(name.lower() + "." + surname.lower() + random.choice(self.EMAIL_PROVIDERS)))
        sql = sql % tuple(val)
        return sql

    def insertUzytkownik(self, number):
        for i in range(number):
            self.cursor.execute(self.genSqlInsertUzytkownik())
            self.db.commit()

    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()