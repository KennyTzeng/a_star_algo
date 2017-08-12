import math
import numpy as np

map_width = 0
map_height = 0
mapList = []
S = None
E = None

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

def calculate_hn(node):
	global E
	return math.sqrt((node.x-E.x)**2 + (node.y-E.y)**2)

def get_lowest_fn(list):
	lowest_fn = 10000000
	for i, node in enumerate(list):
		fn = calculate_gn(node) + calculate_hn(node)
		if(fn < lowest_fn):
			lowest_fn = fn
			lowest_index = i
	return lowest_index

def canMove(node):
	global map_width, map_height, mapList
	list = []
	if(node.x-1 >= 0 and node.y-1 >= 0 and mapList[node.y-1][node.x-1] != '#'):
		list.append((Node(node, node.x-1, node.y-1), 1.4))
	if(node.y-1 >= 0 and mapList[node.y-1][node.x] != '#'):
		list.append((Node(node, node.x, node.y-1), 1))
	if(node.x+1 < map_width and node.y-1 >= 0 and mapList[node.y-1][node.x+1] != '#'):
		list.append((Node(node, node.x+1, node.y-1), 1.4))
	if(node.x-1 >= 0 and mapList[node.y][node.x-1] != '#'):
		list.append((Node(node, node.x-1, node.y), 1))
	if(node.x+1 < map_width and mapList[node.y][node.x+1] != '#'):
		list.append((Node(node, node.x+1, node.y), 1))
	if(node.x-1 >= 0 and node.y+1 < map_height and mapList[node.y+1][node.x-1] != '#'):
		list.append((Node(node, node.x-1, node.y+1), 1.4))
	if(node.y+1 < map_height and mapList[node.y+1][node.x] != '#'):
		list.append((Node(node, node.x, node.y+1), 1))
	if(node.x+1 < map_width and node.y+1 < map_height and mapList[node.y+1][node.x+1] != '#'):
		list.append((Node(node, node.x+1, node.y+1), 1.4))
	return list

def main():
	# load the map
	global mapList, S, E
	lineList = []
	
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

	global map_width, map_height
	map_width = len(mapList[0])
	map_height = len(mapList)

	openList = []
	closedList = []
	openList.append(S)
	while(len(openList) != 0):
		lowest_index = get_lowest_fn(openList)
		n = openList[lowest_index]
		if(n.x == E.x and n.y == E.y):
			return n
		closedList.append(openList.pop(lowest_index))
		for (nTemp, moveCost) in canMove(n):
			gnTemp = calculate_gn(n) + moveCost


def test():
	# load the map
	global mapList
	lineList = []
	
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
	global map_width, map_height
	map_width = len(mapList[0])
	map_height = len(mapList)
	n = Node(None,1,2)
	list = canMove(n)
	print(list)


if(__name__ == '__main__'):
	#main()
	test()