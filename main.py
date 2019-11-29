import mysql.connector as mysql

from ArtykulSql import Artykul
from GrupaWeryfikacjiSql import GrupaWeryfikacji
from KategoriaSql import Kategoria
from RolaSql import Rola
from UzytkownikSql import Uzytkownik
from AutorSql import Autor

DB_NAME = 'seba'
DB_HOST = '185.204.216.201'
DB_USER = 'seba'
DB_PASSWD = '123'


def getDB():
    return mysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, database=DB_NAME)

def printAllValFromTable(table, cursor):
    cursor.execute("SELECT * FROM " + DB_NAME + '.' + table)
    result = cursor.fetchall()
    print(' ----------- VALUES FROM ' + table + ' ----------- ')
    for i in result:
        print(i)
    print(' ------------------------------------ ')


mydb = getDB()
mycursor = mydb.cursor()

#printAllValFromTable('Uzytkownik', mycursor)

uzytkownik = Uzytkownik(mydb, mycursor)
autor = Autor(mydb, mycursor)
kategoria = Kategoria(mydb, mycursor)
grupa_weryfikacji = GrupaWeryfikacji(mydb, mycursor)
rola = Rola(mydb, mycursor)
artykul = Artykul(mydb, mycursor)

#uzytkownik.deleteAllValues()
#autor.deleteAllValues()

#uzytkownik.insertUzytkownik(2000)
#autor.insertAutor(2000)
#kategoria.insertKategoria()
#grupa_weryfikacji.insertGrupaWeryfikacji(100)
#rola.insertRola()
artykul.insertArtykul(1000)



"""printAllValFromTable('Kategoria', mycursor)
printAllValFromTable('GrupaWeryfikacji', mycursor)
printAllValFromTable('Rola', mycursor)"""





