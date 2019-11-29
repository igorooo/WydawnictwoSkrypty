from ArtykulSql import Artykul
from AutorstwoSql import Autorstwo
from GrupaWeryfikacjiSql import GrupaWeryfikacji
from KategoriaSql import Kategoria
from PrzypisanieSql import Przypisanie
from RecenzjaSql import Recenzja
from ReferencjaSql import Referencja
from RolaSql import Rola
from SubskrypcjaSql import Subskrypcja
from UprawnieniaSql import Uprawnienia
from UzytkownikSql import Uzytkownik
from AutorSql import Autor
from WeryfikanciSql import Weryfikanci
from ZadanieWeryfikacyjneSql import ZadanieWeryfikacyjne

class Manager (object):

    def __init__(self, mydb, mycursor):
        self.mydb = mydb
        self.mycursor = mycursor
        self.uzytkownik = Uzytkownik(mydb, mycursor)
        self.autor = Autor(mydb, mycursor)
        self.kategoria = Kategoria(mydb, mycursor)
        self.grupa_weryfikacji = GrupaWeryfikacji(mydb, mycursor)
        self.rola = Rola(mydb, mycursor)
        self.artykul = Artykul(mydb, mycursor)
        self.uprawnienia = Uprawnienia(mydb, mycursor)
        self.subskrypcja = Subskrypcja(mydb, mycursor)
        self.recenzja = Recenzja(mydb, mycursor)
        self.przypisanie = Przypisanie(mydb, mycursor)
        self.zadanie_weryfikacyjne = ZadanieWeryfikacyjne(mydb, mycursor)
        self.weryfikanci = Weryfikanci(mydb, mycursor)
        self.autorstwo = Autorstwo(mydb, mycursor)
        self.referencja = Referencja(mydb, mycursor)

    def fillDB(self, uzytkownik_no=3000, autor_no = 2000, grupa_weryfikacji_no=500, artykul_no = 4000, autorstwo_no=3000):
        self.uzytkownik.insertUzytkownik(uzytkownik_no)
        self.autor.insertAutor(autor_no)
        self.kategoria.insertKategoria()
        self.grupa_weryfikacji.insertGrupaWeryfikacji(grupa_weryfikacji_no)
        self.rola.insertRola()
        self.uprawnienia.insertUprawnienia()
        self.artykul.insertArtykul(artykul_no)
        self.subskrypcja.insertSubskrypcja()
        self.recenzja.insertRecenzja()
        self.przypisanie.insertPrzypisanie()
        self.zadanie_weryfikacyjne.insertZadanieWeryfikacyjne()
        self.weryfikanci.insertWeryfikanci()
        self.autorstwo.insertAutorstwo(autorstwo_no)
        self.referencja.insertReferencja()

    def clearDB(self):
        self.referencja.deleteAllValues()
        self.autorstwo.deleteAllValues()
        self.weryfikanci.deleteAllValues()
        self.zadanie_weryfikacyjne.deleteAllValues()
        self.przypisanie.deleteAllValues()
        self.recenzja.deleteAllValues()
        self.subskrypcja.deleteAllValues()
        self.artykul.deleteAllValues()
        self.uprawnienia.deleteAllValues()
        self.rola.deleteAllValues()
        self.grupa_weryfikacji.deleteAllValues()
        self.kategoria.deleteAllValues()
        self.autor.deleteAllValues()
        self.uzytkownik.deleteAllValues()