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


def main():
	# load the map
	lineList = []
	mapList = []
	S = ()
	E = ()
	with open('map.txt', 'r', encoding='utf-8') as map:
		for i, line in enumerate(map):
			for j, char in enumerate(line):
				if(char == '\n'):
					continue
				if(char == 'S'):
					S = (i, j)
				if(char == 'E'):
					E = (i, j)
				lineList.append(char)
			mapList.append(lineList.copy())
			lineList.clear()



def test():
	a = Node(None, 1, 1)
	b = Node(a, 2, 1)
	c = Node(b, 2, 2)
	print(distance_to_parent(a))
	print(distance_to_parent(b))
	print(distance_to_parent(c))
	print(calculate_gn(a))
	print(calculate_gn(b))
	print(calculate_gn(c))


if(__name__ == '__main__'):
	main()
	#test()