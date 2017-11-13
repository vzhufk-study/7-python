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

table_name = "Cars"


def get_most_value(cursor):
    return cursor.execute("SELECT * FROM %s ORDER BY price DESC " % table_name).fetchone()


def get_sum(cursor):
    return cursor.execute("SELECT SUM(price*qty) as result FROM %s" % table_name).fetchone()[0]


DATABASE_PATH = 'storage/db.sqlite3'

db = sqlite3.connect(DATABASE_PATH)
cursor = db.cursor()
print(get_most_value(cursor))
print(get_sum(cursor))