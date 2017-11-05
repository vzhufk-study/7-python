# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 09.10.2017

data = {}
for i in range(0, int(input("Set amount..."))):
    line = input()
    a, b = line.split()
    data[a] = b
    data[b] = a

print(data[input()])