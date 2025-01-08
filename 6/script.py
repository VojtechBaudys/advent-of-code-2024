import sys
import re

sys.setrecursionlimit(10000000)

def loadInput():
	with open("input.txt") as f:
		s = f.read().strip().split("\n")

	data = []

	for row in s:
		data.append(list(row))

	return data

def findStartPos(arr):
	for row in range(len(arr) - 1):
		for column in range(len(arr[row]) - 1):
			if arr[row][column] == "^":
				return [column, row]

def rotateDirection(direction):
	match direction:
		case [0, -1]:
			return [1, 0]
		case [1, 0]:
			return [0, 1]
		case [0, 1]:
			return [-1, 0]
		case [-1, 0]:
			return [0, -1]
		
def ifFrontObject(arr, frontPosition):
	if not ifInPlayground(arr, frontPosition):
		return False
	if arr[frontPosition[1]][frontPosition[0]] == "#":
		return True
	return False

def ifInPlayground(arr, frontPosition):
	if (frontPosition[0] >= 0 and frontPosition[1]) >= 0 and frontPosition[0] <= len(arr) - 1 and frontPosition[1] <= len(arr[0]) - 1:
		return True
	return False

def countX(arr):
	count = 0

	for row in range(len(arr) - 1):
		for column in range(len(arr[row]) - 1):
			if arr[row][column] == "X":
				count += 1

	return count + 1

def isInLoop(arr, start):
	print("latesrsfasdfasfadfa")

def first(arr):
	count = 0
	run = True
	position = findStartPos(arr)
	direction = [0, -1]
	frontPosition = [position[0] + direction[0], position[1] + direction[1]]

	while(run):
		if ifFrontObject(arr, frontPosition):
			direction = rotateDirection(direction)
			frontPosition = [position[0] + direction[0], position[1] + direction[1]]
		arr[position[1]][position[0]] = "X"
		position = frontPosition
		frontPosition = [position[0] + direction[0], position[1] + direction[1]]
		arr[position[1]][position[0]] = "^"

		if not ifInPlayground(arr, frontPosition):
			run = False
			count = countX(arr)

	print(count)

def second(arr):
	count = 0
	run = True
	position = findStartPos(arr)
	direction = [0 -1]
	frontPosition = [position[0] + direction[0], position[1] + direction[1]]

	while(run):
		if ifFrontObject(arr, frontPosition):
			direction = rotateDirection(direction)
			frontPosition = [position[0] + direction[0], position[1] + direction[1]]

		if isInLoop(arr, position):
			count += 1

		arr[position[1]][position[0]] = "X"
		position = frontPosition
		frontPosition = [position[0] + direction[0], position[1] + direction[1]]
		arr[position[1]][position[0]] = "^"

		if not ifInPlayground(arr, frontPosition):
			run = False

	print(count)

data = loadInput()
first(data)
# data = loadInput()
# second(data)