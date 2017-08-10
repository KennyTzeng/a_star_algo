import math
import numpy as np

class Node:

	def __init__(self, node, x, y):
		self.parent = node
		self.x = (int)(x)
		self.y = (int)(y)
	
def distance_to_parent(node):
	if(node.parent == None):
		return 0
	else:
		return math.sqrt((node.x-node.parent.x)**2 + (node.y-node.parent.y)**2)
def calculate_gn(node):
	if(node.parent == None):
		return 0
	else:
		return calculate_gn(node.parent) + distance_to_parent(node)
def get_lowest_fn(list, E):
	lowest_fn = 10000000
	for i, node in enumerate(list):
		fn = calculate_gn(node) + math.sqrt((node.x-E.x)**2 + (node.y-E.y)**2)
		if(fn < lowest_fn):
			lowest_fn = fn
			lowest_index = i
	return i

def main():
	# load the map
	lineList = []
	mapList = []
	with open('map.txt', 'r', encoding='utf-8') as map:
		for i, line in enumerate(map):
			for j, char in enumerate(line):
				if(char == '\n'):
					continue
				if(char == 'S'):
					S = Node(None, i, j)
				if(char == 'E'):
					E = Node(None, i, j)
				lineList.append(char)
			mapList.append(lineList.copy())
			lineList.clear()

	openList = []
	closedList = []
	openList.append(S)
	while(len(openList) != 0):
		index = get_lowest_fn(openList)
		n = openList[index]
		if(n.x == E.x and n.y == E.y):
			return n
		closedList.append(openList.pop(index))


def test():
	a = Node(None, 1, 1)
	b = Node(a, 2, 1)
	c = Node(b, 2, 2)
	d = Node(None, 1, 1)
	l = []
	l2 = []
	l.append(a)
	l.append(b)
	l.append(c)
	print(l)
	l.remove(a)
	print(l)
	l2.append(l.pop(1))
	print(l)
	print(l2)


if(__name__ == '__main__'):
	#main()
	test()