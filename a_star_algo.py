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

def load_map():
	global mapList, S, E, map_width, map_height
	lineList = []
	
	with open('Map.txt', 'r', encoding='utf-8') as map:
		for i, line in enumerate(map):
			for j, char in enumerate(line):
				if(char == '\n'):
					continue
				if(char == 'S'):
					S = Node(None, j, i)
				if(char == 'E'):
					E = Node(None, j, i)
				lineList.append(char)
			mapList.append(lineList.copy())
			lineList.clear()

	map_width = len(mapList[0])
	map_height = len(mapList)

	
def distance_to_parent(node):
	if(node.parent == None):
		return 0
	else:
		if(math.sqrt((node.x-node.parent.x)**2 + (node.y-node.parent.y)**2) == 1):
			return 1
		else:
			return 1.4
		# return math.sqrt((node.x-node.parent.x)**2 + (node.y-node.parent.y)**2)

def calculate_gn(node):
	if(node.parent == None):
		return 0
	else:
		return calculate_gn(node.parent) + distance_to_parent(node)

def calculate_hn(node):
	global E
	return math.sqrt((node.x-E.x)**2 + (node.y-E.y)**2)

def calculate_fn(node):
	return calculate_gn(node) + calculate_hn(node)

def get_lowest_fn(list):
	lowest_fn = 10000000
	for i, node in enumerate(list):
		fn = calculate_fn(node)
		if(fn < lowest_fn):
			lowest_fn = fn
			lowest_index = i
	return lowest_index

def canMove(node):
	global map_width, map_height, mapList
	list = []
	if(node.x-1 >= 0 and node.y-1 >= 0 and mapList[node.y-1][node.x-1] != '#'):
		list.append(Node(node, node.x-1, node.y-1))
	if(node.y-1 >= 0 and mapList[node.y-1][node.x] != '#'):
		list.append(Node(node, node.x, node.y-1))
	if(node.x+1 < map_width and node.y-1 >= 0 and mapList[node.y-1][node.x+1] != '#'):
		list.append(Node(node, node.x+1, node.y-1))
	if(node.x-1 >= 0 and mapList[node.y][node.x-1] != '#'):
		list.append(Node(node, node.x-1, node.y))
	if(node.x+1 < map_width and mapList[node.y][node.x+1] != '#'):
		list.append(Node(node, node.x+1, node.y))
	if(node.x-1 >= 0 and node.y+1 < map_height and mapList[node.y+1][node.x-1] != '#'):
		list.append(Node(node, node.x-1, node.y+1))
	if(node.y+1 < map_height and mapList[node.y+1][node.x] != '#'):
		list.append(Node(node, node.x, node.y+1))
	if(node.x+1 < map_width and node.y+1 < map_height and mapList[node.y+1][node.x+1] != '#'):
		list.append(Node(node, node.x+1, node.y+1))
	return list

def ifNodesAreTheSame(node1, node2):
	if(node1.parent != None and node2.parent != None):
		return node1.x == node2.x and node1.y == node2.y and ifNodesAreTheSame(node1.parent, node2.parent)
	elif((node1.parent != None and node2.parent == None) or (node1.parent == None and node2.parent != None)):
		return False
	else:
		return node1.x == node2.x and node1.y == node2.y

def ifNodeInList(node, list):
	index = -1
	for i, n in enumerate(list):
		#if(ifNodesAreTheSame(node, n)):
		if(node.x == n.x and node.y == n.y):
			index = i
			break
	return index

def print_path(node):
	path = []
	path.append((node.x, node.y))
	while(node.parent != None):
		node = node.parent
		path.append((node.x, node.y))
	for n in reversed(path):
		print(n, end=" ")
	print()

def algo():
	global S

	load_map()
	
	openList = []
	closedList = []
	openList.append(S)
	while(len(openList) != 0):
		lowest_index = get_lowest_fn(openList)
		n = openList[lowest_index]
		if(n.x == E.x and n.y == E.y):
			return n
		closedList.append(openList.pop(lowest_index))
		
		for nTemp in canMove(n):
			fnTemp = calculate_fn(nTemp)
			indexTemp_o = ifNodeInList(nTemp, openList)
			if(indexTemp_o != -1 and fnTemp > calculate_fn(openList[indexTemp_o])):
				continue
			indexTemp_c = ifNodeInList(nTemp, closedList)
			if(indexTemp_c != -1 and fnTemp > calculate_fn(closedList[indexTemp_c])):
				continue			
			if(indexTemp_o != -1):
				openList.remove(openList[indexTemp_o])
			if(indexTemp_c != -1):
				closedList.remove(closedList[indexTemp_c])
			openList.append(nTemp)

	return None

def main():
	result = algo()
	if(result != None):
		print_path(result)
	else:
		print("there is no solution")


if(__name__ == '__main__'):
	main()