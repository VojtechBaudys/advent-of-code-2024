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

def check(word, text):
	if text == word or text == word[::-1]:
		return True
	else:
		return False

def first(arr):
	word = "XMAS"
	
	count = 0

	for y in range(len(arr)):
		for x in range(len(arr[y])):
			if (not(len(word) > len(arr) - x)):
				if check(word, arr[y][x] + arr[y][x + 1] + arr[y][x + 2] + arr[y][x + 3]): 
					count += 1
			if (not(len(word) > len(arr) - y)):
				if check(word, arr[y][x] + arr[y + 1][x] + arr[y + 2][x] + arr[y + 3][x]): 
					count += 1
			if (not(len(word) > len(arr) - x or len(word) > len(arr) - y)):
				if check(word, arr[y][x] + arr[y + 1][x + 1] + arr[y + 2][x + 2] + arr[y + 3][x + 3]): 
					count += 1
			if (not(len(word) > x + 1 or len(word) > len(arr) - y)):
				if check(word, arr[y][x] + arr[y + 1][x - 1] + arr[y + 2][x - 2] + arr[y + 3][x - 3]): 
					count += 1

	print(count)

def second(arr):
	word = "MAS"
	count = 0

	for y in range(len(arr)):
		for x in range(len(arr[y])):
			a = not(len(word) > len(arr) - x)
			b = not(len(word) > len(arr) - y)

			if not(len(word) > len(arr) - x or len(word) > len(arr) - y):
				if check(word, arr[y][x] + arr[y + 1][x + 1] + arr[y + 2][x + 2]) and check(word, arr[y][x + 2] + arr[y + 1][x + 1] + arr[y + 2][x]):
					count += 1

	print(count)

data = loadInput()
first(data)
data = loadInput()
second(data)