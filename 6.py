# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 26.09.2017
from datetime import datetime, timedelta

from Entities.Student import *

me = Student("Vadym", "Volodumurovich", "Zhufyak", "25-02-1997", "MIT", "402", 1001, 75)
roman_dog = Student("Roman", "Igorovuch", "Baglay", "12-10-1997", "MIT", "402", 0, 3)
roman = Student("Roman", "Yuriyovuch", "Moshnyaga", "15-12-1997", "MIT", "402", 989, 65)
random = Student("Ivan", "Ivanovuch", "Ivanov", "10-10-1998", "MIT", "301", 0, 75)
casual = Student("Alise", "Petrivna", "Kosach", "04-5-1999", "MIT", "102", 1000, 100)
print(str(random) + " age is " + str(random.get_age()))

all_groups = [me, roman_dog, roman, random, casual]
my_group = get_group(all_groups, "402")
print("Sum grant of all groups: " + str(get_sum_grant(all_groups)))
print("Sum grant of my group: " + str(get_sum_grant(my_group)))
print("Average age of all groups: " + str(get_avr_age(all_groups)))
print("Average age of my groups: " + str(get_avr_age(my_group)))
