import mysql.connector as mysql

from ArtykulSql import Artykul
from GrupaWeryfikacjiSql import GrupaWeryfikacji
from KategoriaSql import Kategoria
from RecenzjaSql import Recenzja
from RolaSql import Rola
from SubskrypcjaSql import Subskrypcja
from UprawnieniaSql import Uprawnienia
from UzytkownikSql import Uzytkownik
from AutorSql import Autor

DB_NAME = 'Wydawnictwo'
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
uprawnienia = Uprawnienia(mydb, mycursor)
subskrypcja = Subskrypcja(mydb, mycursor)
recenzja = Recenzja(mydb, mycursor)

#uzytkownik.deleteAllValues()
#autor.deleteAllValues()

#uzytkownik.insertUzytkownik(100)
#autor.insertAutor(100)
#kategoria.insertKategoria()
#grupa_weryfikacji.insertGrupaWeryfikacji(10)
#rola.insertRola()
#uprawnienia.insertUprawnienia()
#artykul.insertArtykul(10)
#subskrypcja.insertSubskrypcja()
#recenzja.insertRecenzja(10)



"""printAllValFromTable('Kategoria', mycursor)
printAllValFromTable('GrupaWeryfikacji', mycursor)
printAllValFromTable('Rola', mycursor)"""





