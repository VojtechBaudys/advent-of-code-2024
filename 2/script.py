import sys

sys.setrecursionlimit(10000000)

def checkRow(row, alowedError):
	row = [int(x) for x in row]
	direction = "asc" if row[0] < row[1] else "desc"

	for i in range(len(row) + 1):
		if (abs(row[i] - row[i - 1])) > 3 or row[i] == row[i - 1]:
			if alowedError:
				row.pop(i)
				return row
			else:
				return False

		if (direction == "asc" and row[i - 1] > row[i]):
			if alowedError:
				row.pop(i)
				return row
			else:
				return False

		if (direction == "desc" and row[i - 1] < row[i]):
			if alowedError:
				row.pop(i)
				return row
			else:
				return False
		
	return True
	
def loadInput():
	with open("input.txt") as f:
		s = f.read().strip().split("\n")

	arr = []
	for row in s:
		arr.append(row.split(" "))

	return arr

def first(arr):
	count = 0

	for row in arr:
		if (checkRow(row, False)): count += 1

	print(count)

def second(arr):
	count = 0

	for row in arr:
		res = checkRow(row, True)
		if type(res) is list:
			if (checkRow(res, False)): count += 1
		elif res:
			count += 1
			
	print(count)

data = loadInput()
first(data)
data = loadInput()
second(data)