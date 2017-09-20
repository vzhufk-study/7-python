# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 05.09.2017
import math

def f(x, a, k):
    return math.sin(x**k)/(a ** (2*k) + math.factorial(2*k))

s = 0

x = float(input("Set x..."))
a = float(input("Set a..."))
e = float(input("Set e..."))

delta = e
k = 0

tmp = f(x, a, k)
k += 1

while delta >= e:
    tmp = f(x, a, k)
    delta = abs(tmp)
    k += 1
    s += tmp

print("Result:" + str(s))
print("In:" + str(k))