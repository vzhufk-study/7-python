# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 22.10.2017

#
# База даних містить інформацію про товари на складі у вигляді:
# назва товару, ціна, кількість на складі, дата приходу товару, номер партії, прізвище і ім’я відповідального.
# Для заданої дати визначте найдорожчий товар, а також підрахуйте загальну вартість товарів на складі.
# В завданні 1 використайте “Об'єктно-орієнтовані бази даних (ZODB)”.
#

from ZODB import FileStorage, DB
from Entities.Product import Product
from datetime import datetime
import transaction

storage = FileStorage.FileStorage('mydata.fs')
db = DB(storage)
connection = db.open()
root = connection.root
if not root.products:
    root.products = {}

n = int(input('Set amount of products...'))
for i in range(n):
    product = Product(
        input("Set product naming..."),
        input("Set product price for piece..."),
        input("Set product amount..."),
        datetime.now(),
        input("Set product set..."),
        input("Set responsible name...")
    )
    try:
        root.products[product.name].amount += product.amount
    except KeyError:
        root.products[product.name] = product

transaction.commit()
print(root.products.keys())
print("Most valuable product is " + Product.get_max_price(list(root.products.values())).name)
print("If storage get on fire you will lose " + str(Product.get_value(list(root.products.values()))))
connection.close()