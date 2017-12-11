# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 23.10.2017


#
# База даних містить інформацію про автомобілі у вигляді: номерний знак, марка авто, модель, рік випуску, вартість,
# пробіг, прізвище і ім’я власника.   Для заданого року випуску знайдіть найдорожчий автомобіль, а також підрахуйте
# загальну вартість усіх автомобілів. В завданні 1 використайте “Об'єктно-орієнтовані бази даних (ZODB)”.
#
import sqlite3

table_name = "Car"


def get_most_value(cursor):
    return cursor.execute("SELECT * FROM %s ORDER BY price DESC " % table_name).fetchone()


def get_sum(cursor):
    return cursor.execute("SELECT SUM(price) as result FROM %s" % table_name).fetchone()[0]

def init(cursor):
    return cursor.execute("""CREATE TABLE %s(
                          number VARCHAR(6),
                          mark VARCHAR(64),
                          model VARCHAR(64),
                          year INT,
                          price FLOAT,
                          in_run FLOAT,
                          owner VARCHAR(128),
                          PRIMARY KEY (number));""" % table_name)

def seed(cursor):
    cursor.execute("INSERT INTO %s VALUES ('VF231F', 'Audi', 'A4', 2008, 8000, 23000, 'Baglay Roman')" % table_name)
    cursor.execute("INSERT INTO %s VALUES ('VF222F', 'Nuva', '1A', 1997, 100, 223000, 'Moshnyaga Roman')" % table_name)
    cursor.execute("INSERT INTO %s VALUES ('DF321A', 'Nisan', 'ATO', 2000, 5100, 3000, 'Me')" % table_name)

DATABASE_PATH = 'db.sqlite3'

db = sqlite3.connect(DATABASE_PATH)
cursor = db.cursor()
print(get_most_value(cursor))
print(get_sum(cursor))
# init(cursor)
# seed(cursor)