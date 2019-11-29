import mysql.connector as mysql
from Manager import Manager

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

manager = Manager(mydb, mycursor)

#manager.clearDB()
manager.fillDB()

#manager.uzytkownik.insertUzytkownik(100)



