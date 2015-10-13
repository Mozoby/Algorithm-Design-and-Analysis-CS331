import random 
import math

'''
Greedy and Backtracking Coloring of Sparse Graphs
Author: Bryan Thornbury
'''

def randGraph(n,m,d):
	colors = [i%d for i in xrange(n)]
	graph = [[] for i in xrange(n)]
	edgeCount = 0
	for e in xrange(10*m):
		if(edgeCount >= m): break

		v1 = random.randint(0,n-1)
		v2 = random.randint(0,n-1)

		if(colors[v1] != colors[v2]): 
			edgeCount += 1
			graph[v1].append(v2)
			graph[v2].append(v1)

	if(edgeCount == m): return graph
	return None


#graph in form of adjacency list
#returns number of colors used
def greedy(graph):
	colors = [None for x in xrange(len(graph))]

	#shuffle the graph, but keep track of original index
	shuffledGraph = zip(xrange(len(graph)), graph)
	random.shuffle(shuffledGraph)

	maxColor = 0
	for node in shuffledGraph:
		vertex = node[0]
		edges = node[1]
		colors[vertex] = greedy_color(graph, colors, vertex)
		maxColor = max(maxColor, colors[vertex])

	#print validate_coloring(graph,colors)
	return maxColor + 1

#Colors indexed by 0 .. infinity
def greedy_color(graph, colors, current):
	available = [True for i in xrange(len(graph))]
	for dest in (x for x in graph[current] if colors[x] != None):
		available[colors[dest]] = False

	for index in xrange(len(available)):
		if(available[index]): return index

	return len(available)

# def greedy_dfs(graph, colors, current, visited):
# 	#process current node
# 	visited[current] = True

# 	colors[current] = greedy_color(graph, colors, current)

# 	ret = (colors, colors[current])

# 	#visit all children
# 	for child in graph[current]:
# 		if not visited[child]: 
# 			nRet =  greedy_dfs(graph, colors, child, visited)
# 			ret = (nRet[0], max(ret, nRet[1]))

# 	return ret

def validate_coloring(graph, colors):
	for vertex in xrange(len(graph)):
		for v2 in graph[vertex]:
			if(colors[vertex] == colors[v2]): return False

	return True

def backtrack(graph, color_count):
	colors = [None for x in xrange(len(graph))]

	return backtrack_recurse(graph, colors, 0, color_count)[0]

def backtrack_recurse(graph, colors, current, color_count):
	#Past end, don't count this node
	if(current == len(graph)): return (0, True)

	nodeCount = 1

	availableColors = [True for i in xrange(color_count)]

	#determine available colors from neighbors
	for dest in (x for x in graph[current] if colors[x] != None):
		availableColors[colors[dest]] = False

	#Try each available color and go to the next one
	for color,available in enumerate(availableColors):
		#Try a color
		if(available):
			colors[current] = color
			nextStep = backtrack_recurse(graph, colors, current + 1, color_count)
			nodeCount += nextStep[0]

			if(nextStep[1]): 
				#if(current == 0): print validate_coloring(graph, colors)
				#if(current == 0): print colors
				return (nodeCount, True)


	#No colors worked, go back!
	colors[current] = None

	return (nodeCount, False)

def execute_greedy():
	print "Greedy Method"
	print "Order\tColors"
	m = lambda x: int(5 * x * math.log(x,10))

	for i in xrange(10,101, 10):
		colorSum = 0
		for j in xrange(10):
			graph = None
			while graph is None:
				graph = randGraph(i, m(i), 7)
			colorSum += greedy(graph)

		print str(i) + "\t" + str(colorSum / 10.0)

	for i in xrange(100, 1001, 100):
		colorSum = 0
		for j in xrange(10):
			graph = None
			while graph is None:
				graph = randGraph(i, m(i), 7)
			colorSum += greedy(graph)

		print str(i) + "\t" + str(colorSum / 10.0)

	print ""

def execute_backtracking():
	print "Backtracking Method"
	print "Order\tNodes"
	m = lambda x: int(5 * x * math.log(x,10))

	for i in xrange(10,33):
		nodeSum = 0
		for j in xrange(10):
			graph = None
			while graph is None:
				graph = randGraph(i, m(i), 7)
			nodeSum += backtrack(graph, 7)

		print str(i) + "\t" + str(nodeSum / 10.0)


	print ""

if __name__ == "__main__":
	execute_greedy()
	execute_backtracking()






















