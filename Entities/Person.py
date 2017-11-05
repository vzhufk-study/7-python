# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 10.10.2017

from datetime import datetime


class Person:
    def __init__(self, first_name, middle_name, last_name, birth_date):
        self.first_name = str(first_name)
        self.middle_name = str(middle_name)
        self.last_name = str(last_name)
        self.birth_date = datetime.strptime(birth_date, "%d-%m-%Y")

    def get_age(self):
        return int((datetime.now() - self.birth_date).days / 365.25)

    def __str__(self):
        return " ".join([self.first_name, self.middle_name, self.last_name])
