# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 26.09.2017
from datetime import datetime, timedelta


class Person:
    def __init__(self, first_name, middle_name, last_name, birth_date):
        self.first_name = str(first_name)
        self.middle_name = str(middle_name)
        self.last_name = str(last_name)
        self.birth_date = datetime.strptime(birth_date, "%d-%m-%Y")

    def getAge(self):
        return (datetime.now().day - self.birth_date.day) // 365.25


class Student(Person):
    def __init__(self, first_name, middle_name, last_name, birth_date, faculty, group, grant, avr_mark):
        super().__init__(first_name, middle_name, last_name, birth_date)
        self.faculty = str(faculty)
        self.group = str(group)
        self.grant = float(grant)
        self.avr_mark = float(avr_mark)


def getGroup(objects, group):
    result = []
    for i in objects:
        if i.group == group:
            result.append(i)
    return result


def getSumGrant(objects):
    result = 0
    for i in objects:
        result += i.grant
    return result


def getAvrAge(objects):
    result = 0
    for i in objects:
        result += i.getAge()
    return result / len(objects)


me = Student("Vadym", "Volodumurovich", "Zhufyak", "25-02-1997", "MIT", "402", 1001, 75)
neighbor = Student("Roman", "Igorovuch", "Baglay", "12-10-1997", "MIT", "402", 0, 3)
neighbor_tmp = Student("Roman", "Yuriyovuch", "Moshnyaga", "15-12-1997", "MIT", "402", 989, 65)

print(me.getAge())

bratishki = [me, neighbor, neighbor_tmp]
bratishki = getGroup(bratishki, "402")
print(getSumGrant(bratishki))
print(getAvrAge(bratishki))