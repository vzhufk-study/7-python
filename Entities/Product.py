# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 24.10.2017
import persistent


class Product(persistent.Persistent):

    def __init__(self, name, price, amount, date, set, responsible_name):
        self.name = str(name)
        self.price = float(price)
        self.amount = int(amount)
        self.date = date
        self.set = str(set)
        self.responsible_name = str(responsible_name)

    @staticmethod
    def get_max_price(objects):
        result = None
        for i in objects:
            if not result or i.price > result.price:
                result = i
        return result

    @staticmethod
    def get_value(objects):
        result = 0
        for i in objects:
            result += i.price * i.amount
        return result
