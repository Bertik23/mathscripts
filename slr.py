from fractions import Fraction
from copy import deepcopy
from pprint import pprint
from sympy import sympify


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

# matrix = [
#     [1, 1, 5],
#     [1, -1, 1]
# ]

# matrix = [
#     [2, -1, 1, 0],
#     [1, 2, -2, 0],
#     [3, 1, -1, 0]
# ]

# 4g
# matrix = [
#     [1, -3, -26, 22, 0],
#     [1, 0, -8, 7, 0],
#     [1, 1, -2, 2, 0],
#     [4, 5, -2, 3, 0]
# ]

# # 3j
# matrix = [
#     [1, 1, 2, 4],
#     [1, -2, 1, 0],
#     [1, -5, 0, -4]
# ]

# 4c
# matrix = [
#     [2, 1, -1, 1, 1],
#     [3, -2, 2, -3, 2],
#     [2, -1, 1, -3, 4],
#     [5, 1, -1, 2, -1]
# ]

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


# def matrixNotTriangularFrom(matrix):
#     # print(len(matrix[0]))
#     zeros = len(matrix) - 1
#     for i in range(len(matrix[0])):
#         for a in reversed(range(len(matrix))):
#             # print(a, i, len(matrix)-a, zeros)
#             if matrix[a][i] != 0 and len(matrix)-a <= zeros:
#                 return a, i
#         zeros -= 1
#     return None, None


def matrixNotTriangularFrom(matrix):
    rowZeros = []
    for row in matrix:
        zeros = 0
        for a in row:
            if a == 0:
                zeros += 1
            else:
                break
        rowZeros.append(zeros)

    for i, z in enumerate(reversed(rowZeros)):
        if i == len(rowZeros)-1:
            continue
        if z <= rowZeros[-i-2]:
            print(rowZeros, len(rowZeros)-1-i, z, -i)
            return len(rowZeros)-1-i, z


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


# def makeMatrixUpperTriangular(data):
#     for column in range(len(data[0])-1):
#         pocet_nul = len(data) - 1 - column
#         for radek in range(pocet_nul):
#             nasobitel = data[column][column]
#             # číslo které vynásobíme n a přičteme k nulaku
#             pos = len(data) - radek - 1
#             nulak = data[pos][column]
#             # číslo které chceme dát na 0

#             try:
#                 nasobek = Fraction(-nulak, nasobitel)
#                 # - nulak / nasobitel
#             except ZeroDivisionError:
#                 nasobek = 0

#             for i in range(len(data[pos])):
#                 data[pos][i] += data[column][i] * nasobek
#     return data


def check_hodnosti(A, Ab, n):
    '''
        zkontroluje kolik má matice řešení a vyprintuje info
    '''
    if A < Ab:
        print("SLR nemá řešení")
        return -1
    elif A == Ab == n:
        print("SLR má právě jedno řešení")
        return 0
    elif A == Ab and A < n:
        print("SLR má nekonečně mnoho řešení")
        return n-A


def zerosToInt(matrix):
    out = deepcopy(matrix)
    for i, row in enumerate(out):
        for ii, a in enumerate(row):
            if a == 0:
                out[i][ii] = 0
    return out


def makeMatrixUpperTriangular(matrix):
    out = deepcopy(matrix)
    while not isMatrixTriangular(out):
        pprint(out)
        out = removeZeroRows(out)
        r, s = matrixNotTriangularFrom(out)
        k = Fraction(-out[r][s], out[r-1][s])
        for i, a in enumerate(out[r]):
            out[r][i] = a + out[r-1][i]*k

    return out


def solve_parametry(matice, rights, pocet_parametru):
    '''
        vyřeší matici pomocí parametrů
    '''
    data = [[*row, rights[i]] for i, row in enumerate(matice)]
    par = 0
    # odstranění nulových řádků
    parametry = [None for i in range(len(data[0])-1)]
    for line in data[::-1]:
        if line != [0 for i in range(len(line))]:
            for j, num in enumerate(line[:-1]):
                if num != 0 and par < pocet_parametru and parametry[j] is None:
                    parametry[j] = chr(97 + par)
                    par += 1
                elif parametry[j] is None and num != 0:
                    # vyjádření neznámých pomocí parametrů
                    val = str(line[-1])
                    for x in range(len(line[:-1])):
                        if x != j and parametry[x] is not None:
                            # val += str("-" + str(line[x]) + "*"
                            #  +str(parametry[x]))
                            val += f"-{str(line[x])}*({str(parametry[x])})"
                    parametry[j] = val
    return parametry


matrix = makeMatrixUpperTriangular(matrix)
matrix = zerosToInt(matrix)

pprint(matrix)
matrix = removeZeroRows(matrix)

hodnostAb = len(matrix)

rights = []
for i, r in enumerate(matrix):
    rights.append(matrix[i].pop())

pprint(matrix)
pprint(rights)

numOfSolutions = None
matrix, rs = removeZeroRows(matrix, True)
for i, r in enumerate(rs):
    rights.pop(r-i)

hodnostA = len(matrix)

numOfSolutions = check_hodnosti(hodnostA, hodnostAb, len(matrix[0]))

results = {}
if numOfSolutions == 0:
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

elif numOfSolutions > 0:
    results = solve_parametry(matrix, rights, numOfSolutions)
    for i, r in enumerate(results):
        results[i] = sympify(r)


print(results)
