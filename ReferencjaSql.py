import names
import random
import string

DB_NAME = 'Wydawnictwo'

class Referencja(object):
    TABLE = 'Referencja'


    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor
        self.articles = self.getArtykulArr()

    def getArtykulArr(self):
        self.cursor.execute("SELECT DISTINCT(idArtykul) FROM " + DB_NAME + ".Artykul")
        result = self.cursor.fetchall()
        return result

    def getTupleOfArtykul(self):
        art1 = random.choice(self.articles)
        art2 = random.choice(self.articles)

        while art1 == art2:
            art2 = random.choice(self.articles)
        return art1, art2


    def genSqlReferencja(self, num):
        sql = "INSERT INTO `Wydawnictwo`.`Referencja` (`Artykul_idArtykulReferujacy`, `Artykul_idArtykulReferowany`) VALUES (%s, %s);"
        sqlArr = []
        randNum = random.randint(0, 3)
        art1 = self.articles[num]
        articles2 = self.articles[:]
        articles2.remove(art1)

        for i in range(randNum):
            art2 = random.choice(articles2)
            articles2.remove(art2)
            val = (art1[0], art2[0])
            sqlArr.append(sql % val)


        return sqlArr

    def insertReferencja(self):
        maxArt = len(self.articles)
        for i in range(len(self.articles)):
            sqlArr = self.genSqlReferencja(i)
            for sql in sqlArr:
                self.cursor.execute(sql)
                self.db.commit()


    def deleteAllValues(self):
        self.cursor.execute("DELETE FROM " + DB_NAME + "." + self.TABLE)
        self.db.commit()
