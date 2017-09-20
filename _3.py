# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 19.09.2017


def getVectorRow(matrix, getRow):
    result = []
    for i in matrix:
        result.append(getRow(i))
    return result


def getVectorCol(matrix, getCol):
    result = []
    for i in range(0, len(matrix[0])):
        tmp = []
        for j in range(0, len(matrix)):
            tmp.append(matrix[j][i])
        result.append(getCol(tmp))
    return result


def getVectorSum(vector):
    result = 0
    for i in vector:
        result += i
    return result


def printBy(array, amount=5):
    line = ""
    for key, value in enumerate(array):
        line += str(value) + " "
        if (key + 1) % amount == 0:
            print(line)
            line = ""
    print(line)


n = int(input("Set size of matrix..."))
n = 15 if n > 15 else n

matrix = []

for i in range(0, n):
    matrix.append([])
    for j in range(0, n):
        matrix[i].append(int(input()))

resultA = getVectorRow(matrix, getVectorSum)
resultB = getVectorCol(matrix, getVectorSum)

printBy(resultA)
printBy(resultB)
