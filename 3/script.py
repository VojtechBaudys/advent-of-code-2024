import sys
import re

sys.setrecursionlimit(10000000)

def loadInput():
	with open("input.txt") as f:
		s = f.read().strip().split("\n")

	return s[0]

def fn(string):
	count = 0
	do = True
	stringArr = re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", string)

	for e in stringArr:
		match e:
			case "don't()":
				do = False
			case "do()":
				do = True
			case _:
				if do:
					e = e.split("(")[1].split(")")[0].split(",")
					count += int(e[0]) * int(e[1])

	print(count)

data = loadInput()
fn(data)