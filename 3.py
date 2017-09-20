def getVector(matrix, getRow):
    result = []
    for i in matrix:
        result.append(getRow(i))
    return result

n = int(input("Set size of matrix..."))

matrix = []

for i in range(0, n):
    matrix.append([])
    for j in range(0, n):
        matrix[i].append(int(input()))

a = int(input("Set a..."))
b = int(input("Set b..."))

def getVectorRow(row, a=a, b=b):
    result = 0
    for i in row:
        if a <= abs(i) <= b:
            result += i*i
    return result

result = getVector(matrix, getVectorRow)

while len(result) > 4:
    print(result[0:5])
    result = result[5:]
print(result)
