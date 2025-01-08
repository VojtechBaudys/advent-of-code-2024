import sys

sys.setrecursionlimit(10000000)

def loadInput():
	with open("input.txt") as f:
		s = f.read().strip().split("\n")

	left = []
	right = []

	for row in s:
		split = row.split()

		left.append(int(split[0]))
		right.append(int(split[1]))

	return {"left": left, "right": right}

def first(arr1, arr2):
	count = 0
	for _ in range(len(arr1)):
		count += abs(min(arr1) - min(arr2))

		arr1.remove(min(arr1))
		arr2.remove(min(arr2))

	print(count);

def second(arr1, arr2):
	count = 0

	for number in arr1:
		sameCount = arr2.count(number)
		count += number * sameCount

	print(count);

data = loadInput()
first(data["left"], data["right"])
data = loadInput()
second(data["left"], data["right"])
