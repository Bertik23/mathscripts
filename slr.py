# from fractions import Fraction
from copy import deepcopy
from pprint import pprint
from sympy import Symbol

matrix = [
          [3, 2, 1, 1],
          [-4, 5, -2, 2],
          [5, -1, 2, 0],
          [2, -3, -1, 9]
         ]


matrix = [
    [1, 2, 1, 1, 0],
    [1, 3, 0, 2, 0],
    [0, 1, -1, 1, 0]
]

matrix = [
    [1, 1, 5],
    [1, -1, 1]
]

matrix = [
    [2, -1, 1, 0],
    [1, 2, -2, 0],
    [3, 1, -1, 0]
]

# 3j
matrix = [
    [1, 1, 2, 4],
    [1, -2, 1, 0],
    [1, -5, 0, -4]
]

# matrix = [
#           [3, 2, 1, 1],
#           [0, 5, -2, 2],
#           [0, 0, 0, 1],
#           [0, 0, 0, 0]
#          ]


def isMatrixTriangular(matrix):
    lastRowZeros = -1
    for row in matrix:
        rowZeros = 0
        for i in row:
            if i == 0:
                rowZeros += 1
            else:
                break
        if rowZeros > lastRowZeros:
            lastRowZeros = rowZeros
        else:
            return False
    return True


def matrixNotTriangularFrom(matrix):
    # print(len(matrix[0]))
    zeros = len(matrix) - 1
    for i in range(len(matrix[0])):
        for a in reversed(range(len(matrix))):
            # print(a, i)
            if matrix[a][i] != 0 and len(matrix)-a <= zeros:
                return a, i
        zeros -= 1
    return None, None


def removeZeroRows(matrix, returnIndexes=False):
    m = deepcopy(matrix)
    rows = []
    zero = [0] * len(m[0])
    for i, row in enumerate(m):
        if row == zero:
            rows.append(i)

    for i, r in enumerate(rows):
        m.pop(r-i)

    if returnIndexes:
        return m, rows
    return m


while not isMatrixTriangular(matrix):
    r, s = matrixNotTriangularFrom(matrix)
    k = -matrix[r][s] / matrix[r-1][s]
    for i, a in enumerate(matrix[r]):
        matrix[r][i] = a + matrix[r-1][i]*k

pprint(matrix)
matrix = removeZeroRows(matrix)


rights = []
for i, r in enumerate(matrix):
    rights.append(matrix[i].pop())

pprint(matrix)
pprint(rights)

numOfSolutions = None
matrix, rs = removeZeroRows(matrix, True)
for i, r in enumerate(rs):
    if x := rights.pop(r-i) == 0:
        numOfSolutions = 0

results = {}
if numOfSolutions != 0:
    row = len(matrix)-1
    n = len(matrix[0])-1
    print(row, n)
    if n == row:
        while n >= 0:
            print(n)
            x = results[n] = round(rights[row]/matrix[row][n], 5)
            for i, r in enumerate(matrix):
                rights[i] -= r[n]*x
            n -= 1
            row -= 1
            if row < 0 or n < 0:
                break

    if n > row:
        print(n-row)


print(results)


print(matrixNotTriangularFrom(matrix))
print(isMatrixTriangular(matrix))
