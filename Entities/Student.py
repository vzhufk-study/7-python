# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 10.10.2017
from Entities.Person import Person


class Student(Person):
    def __init__(self, first_name, middle_name, last_name, birth_date, faculty, group, grant, avr_mark):
        super().__init__(first_name, middle_name, last_name, birth_date)
        self.faculty = str(faculty)
        self.group = str(group)
        self.grant = float(grant)
        self.avr_mark = float(avr_mark)


def get_group(objects, group):
    result = []
    for i in objects:
        if i.group == group:
            result.append(i)
    return result


def get_sum_grant(objects):
    result = 0
    for i in objects:
        result += i.grant
    return result


def get_avr_age(objects):
    result = 0
    for i in objects:
        result += i.get_age()
    return result / len(objects)
