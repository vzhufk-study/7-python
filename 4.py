# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 26.09.2017
import math

n = int(input("n > "))
m = int(input("m > "))


def sqrtFactRecursion(i):
    sqrt = 1.0 / math.factorial(i)
    if i < n:
        sqrt += sqrtFactRecursion(i + 1)
    result = 1.0 / 8 * math.sqrt(sqrt)
    return result


delimiter = sqrtFactRecursion(1)
remainder = 2 ** m
print("Delimiter = " + str(delimiter))
print("Reminder = " + str(remainder))
print(remainder/delimiter)