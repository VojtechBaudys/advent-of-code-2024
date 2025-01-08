import sys
import math

sys.setrecursionlimit(10000000)

def loadInput():
	top = []
	bottom = []

	with open("topRule.txt") as f:
		t = f.read().strip().split("\n")
		
	for i in t:
		s = i.split("|")
		top.append([int(s[0]), int(s[1])])

	with open("bottomRule.txt") as f:
		b = f.read().strip().split("\n")

	for i in b:
		s = i.split(",")
		bottom.append([int(x) for x in s])

	return top, bottom

def ifValid(topRules, bottomRule):
	for sec in range(0, len(bottomRule) - 1):
		secArrs = [x for x in topRules if x[1] == bottomRule[sec]]

		for first in range(sec, len(bottomRule) - 1):
			for secArr in secArrs:
				if secArr[0] == bottomRule[first + 1]:
					return False
	return True

def reorder(topRules, bottomRule):
	for sec in range(0, len(bottomRule) - 1):
		secArrs = [x for x in topRules if x[1] == bottomRule[sec]]

		for first in range(sec, len(bottomRule) - 1):
			for secArr in secArrs:
				if secArr[0] == bottomRule[first + 1]:
					bottomRule[first + 1] = secArr[1]
					bottomRule[sec] = secArr[0]
					return bottomRule

def first(topRules, bottomRules):
	count = 0

	for bottomRule in bottomRules:
		if ifValid(topRules, bottomRule):
			count += bottomRule[math.ceil(len(bottomRule) / 2 - 1)]

	print(count)

def second(topRules, bottomRules):
	count = 0

	for bottomRule in bottomRules:
		iteration = 0
		newBottomRule = bottomRule

		while not ifValid(topRules, bottomRule):
			newBottomRule = reorder(topRules, newBottomRule)
			iteration += 1

		if iteration != 0:
			count += bottomRule[math.ceil(len(bottomRule) / 2 - 1)]

	print(count)

data = loadInput()
first(data[0], data[1])
data = loadInput()
second(data[0], data[1])