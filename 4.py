# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 19.09.2017

n = int(input())

data = {}
for i in range(0, n):
    line = input()
    line = line.split()
    data[line[0]] = line[1:]

n = int(input())

for i in range(0, n):
    line = input()
    for key, value in data.items():
        if line in value:
            print(key)
            break
