import random

DB_NAME = 'Wydawnictwo'

class Subskrypcja(object):
    TABLE = 'Subskrypcja'

    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor

    def addQuotes(self, val):
        return "'" + str(val) + "'"


    def randomDate(self):
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2018, 2019)
        return (year, month, day)

    def randomNextDate(self, date):
        year = date[0]
        month = date[1]
        day = date[2]

        dayDiff = 28-day
        monthDiff = 12 - month
        yearDiff = 2019 - year

        nextDate = (year,month,day)

        if dayDiff == 0:
            if monthDiff == 0:
                if yearDiff == 0:
                    return nextDate
                else:
                    return (year + random.randint(0, yearDiff), month, day)
            else:
                return (year, month + random.randint(0, monthDiff), day)
        else:
            return (year, month, day + random.randint(0, dayDiff))

    def getDateFromTouple(self, date):
        return str(date[0])+'-'+str(date[1])+'-'+str(date[2])

    def getMaxIntVal(self, table, column):
        self.cursor.execute("SELECT MAX(" + column + ") FROM " + DB_NAME + '.' + table)
        result = self.cursor.fetchall()
        for i in result:
            if(i[0] == None):
                return 0
            maxIntVal = (int)(i[0])
        return maxIntVal


    def genSqlInsertSubskrypcja(self, idUzytkownik):
        id = self.getMaxIntVal("Subskrypcja", 'idSubskrypcja') + 1
        sql = "INSERT INTO `Wydawnictwo`.`Subskrypcja` (`idSubskrypcja`, `Uzytkownik_idUzytkownik`, `Start`, `Koniec`) VALUES (%s, %s, %s, %s);"

        dateS = self.randomDate()
        dateE = self.randomNextDate(dateS)

        val = [id, idUzytkownik, self.addQuotes(self.getDateFromTouple(dateS)), self.addQuotes(self.getDateFromTouple(dateE))]
        return sql % tuple(val)

    def insertSubskrypcja(self):
        max = self.getMaxIntVal('Uzytkownik', 'idUzytkownik')
        i = 1
        while i < max:
            sql = self.genSqlInsertSubskrypcja(i)
            self.cursor.execute(sql)
            self.db.commit()
            i += random.randint(1, 3)


    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()
