# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 19.09.2017

n = int(input())

data = {}
for i in range(0, n):
    line = input()
    line = line.split()
    for j in line[1:]:
        data[j] = line[0]

n = int(input())

for i in range(0, n):
    line = input()
    try:
        print(data[line])
    except KeyError:
        print("No such city in DB.")
