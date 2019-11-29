import names
import random
import string

DB_NAME = 'Wydawnictwo'

class Artykul(object):
    TABLE = 'Artykul'
    STAGE = ['Recenzja', 'Weryfikacja', 'Redakcja', 'Publikacja']
    AVAILABILITY = ['Platny', 'Darmowy']
    KEY_WORDS = ['science', 'math', 'quantum engineering', 'machine learning', 'artificial intelligence', 'biology',
                 'law', 'american law', 'economy', 'poland', 'equations', 'c++', 'assembler', 'pils', 'testing',
                 'space', 'black holes', 'music', 'art']
    FILE = 'data/SampleArticle.pdf'


    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor
        self.article = self.convertToBinaryData()


    def addQuotes(self, val):
        return "'" + str(val) + "'"

    def randomString(self, stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def randomDateP(self):
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(1990, 2019)
        return (year, month, day)

    def randomDateD(self):
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

    def convertToBinaryData(self):
        with open(self.FILE, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def getMaxIntVal(self, table, column):
        self.cursor.execute("SELECT MAX(" + column + ") FROM " + DB_NAME + '.' + table)
        result = self.cursor.fetchall()
        for i in result:
            if(i[0] == None):
                return 0
            maxIntVal = (int)(i[0])
        return maxIntVal

    def genKeyWords(self):
        keywords = ''
        number = random.randint(2, 10)
        for i in range(number):
            keywords = keywords + random.choice(self.KEY_WORDS)
            if(i < number-1):
                keywords += ', '
        return keywords

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


    def genSqlInsertArtykul(self):
        id = self.getMaxIntVal(self.TABLE, 'idArtykul') + 1
        no_of_versions = random.randint(1, 5)
        sqlArr = []
        sql = "INSERT INTO `Wydawnictwo`.`Artykul` (`idArtykul`, `Wersja`, `Nazwa`, `Data dodania`, `Etap`, `Treść`," \
              " `Data publikacji`, `Dostepnosc`, `SlowaKluczowe`, `Kontrybutor`) VALUES (%s, %s, %s, %s, %s, %s, %s," \
              " %s, %s, %s);"

        version = 1
        name = 'Article about ' + names.get_last_name() + ' effect'
        dateD = self.randomDateD()
        dateP = self.randomDateP()
        pdf = self.article
        availability = random.choice(self.AVAILABILITY)
        keywords = self.genKeyWords()
        k = self.getRandomKontrybutor()

        val = [id, 1, self.addQuotes(name), '', '', pdf, '',
               availability, self.addQuotes(keywords), k]

        for i in range(1, no_of_versions+1):
            stage = 'Archiwizacja'
            if( i < version):
                stage = 'Archiwizacja'
            else:
                stage = random.choice(self.STAGE)

            dateD = self.randomNextDate(dateD)
            dateP = self.randomNextDate(dateP)

            val[1] = i
            val[3] = self.getDateFromTouple(dateD)
            val[4] = stage
            val[6] = self.getDateFromTouple(dateP)
            sqlArr.append(sql % tuple(val))

            val1 = val
            val[5] = 'pdf file'

            self.cursor.execute(sql, val)
            self.db.commit()

        return sqlArr

    def insertArtykul(self, number):
        for i in range(number):
            sqlArr = self.genSqlInsertArtykul()


    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()



#a = Artykul(1,2)

#a.insertArtykul(1)
