
print '''
CS 331 Project 1
Optimal Binary Tree Implementation
Author: Bryan Thornbury
'''

def memoize(f):
	recorded = dict()
	def call(*args, **kwargs):
		if('clear' in kwargs and kwargs['clear']): recorded.clear()

		if(not args[1:] in recorded): recorded[args[1:]] = f(*args)
		
		return recorded[args[1:]]
	return call

def computeAverageProb(node, depth = 1):
	return (lambda:(node[0][1] * depth) + reduce(lambda x,y: x+y, [computeAverageProb(n, depth+1) for n in node[1:3]]), lambda:0)[node is None]()

@memoize
def optimalBinaryTree(arr,lb, rb):
	if(lb == rb): return (arr[lb], None, None)

	minTree = None
	minCost = float("inf")

	for root in range(lb,rb+1):
		#compute min right subtree
		right = optimalBinaryTree(arr, root+1, rb)

		#compute min left subtree
		left = optimalBinaryTree(arr, lb,root-1)

		candidateCost = computeAverageProb((arr[root],left,right))
		if(candidateCost < minCost):
			minTree = (arr[root],left,right)
			minCost = candidateCost
	return minTree

def stringifyTree(node):
	if(node is None): return ""

	if(node[1] is None and node[2] is None): return node[0][0]
	
	return node[0][0] + '(' + stringifyTree(node[1]) + ',' + stringifyTree(node[2]) + ')'


tests = [[('Don', 3/8.0), ('Isabelle', 3/8.0), ('Ralph', 1/8.0), ('Wally', 1/8.0)],
		[('A', 0.1), ('B', 0.2), ('C', 0.4), ('D', 0.3)],
		[('A',1/7.0),('B',1/7.0),('C',1/7.0),('D',1/7.0),('E',1/7.0),('F',1/7.0),('G',1/7.0)]]

print '\n'.join([' => '.join([str(computeAverageProb(tree)), stringifyTree(tree)]) for tree in [optimalBinaryTree(t,0,len(t)-1, clear=True) for t in tests]])
# for t in tests:
# 	#Clear memoization
# 	optimalBinaryTree(clear=True)
# 	result = optimalBinaryTree(t,0,len(t)-1)
# 	print  computeAverageProb(result),  stringifyTree(result)
