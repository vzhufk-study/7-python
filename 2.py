# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 05.09.2017

a = input("Text 1:")
b = input("Text 2:")

for i in b.split():
    a = a.replace(i, "")

print(a)