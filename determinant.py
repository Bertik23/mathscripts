matrix = [
	[-2, -1, 0, 1],
	[0, 1, -2, -1],
	[0, 0, 3, -2],
	[0, 0, 0, 4]
]

matrix = [[24, -18, 36],
		[32, 12, 0],
		[36,27, 54]]

matrix = [
	[1, 2, 0, -1],
	[3, 0, 1, 4],
	[2, 4, 0, -2],
	[-1, 5, 0, 2]
]

def calcDeterminant(matrix):
	out = 0
	outTxt = ""
	for _ in range(len(matrix)):
		mid = 0
		midTxt = ""
		for i, row in enumerate(matrix):
			if i == 0:
				mid = row[i]
				midTxt = str(row[i])
			else:
				mid *= row[i]
				midTxt += f"*{row[i]}"
		out += mid
		outTxt += f" + {midTxt}"
		for i, row in enumerate(matrix):
			matrix[i].append(matrix[i].pop(0))

	for _ in range(len(matrix)):
		mid = 0
		midTxt = ""
		for i, row in enumerate(matrix):
			if i == 0:
				mid = row[-i-1]
				midTxt = str(row[-i-1])
			else:
				mid *= row[-i-1]
				midTxt += f"*{row[-i-1]}"
		out -= mid
		outTxt += f" - {midTxt}"
		for i, row in enumerate(matrix):
			matrix[i].append(matrix[i].pop(0))

	return out, outTxt

print(calcDeterminant(matrix))


