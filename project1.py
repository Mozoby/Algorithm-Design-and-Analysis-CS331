
print '''
CS 331 Project 1
Optimal Binary Tree Implementation
Author: Bryan Thornbury
'''

def memoize(f):
	recorded = dict()
	def call(*args, **kwargs):
		if('clear' in kwargs and kwargs['clear']): 
			recorded.clear()
			return
		if(args[1:] in recorded):
			return recorded[args[1:]]
		else:
			recorded[args[1:]] = f(*args)
			return recorded[args[1:]]
	return call

def computeAverageProb(node, depth = 1):
	if(node is None): 
		return 0
	return (node[0][1] * depth) + reduce(lambda x,y: x+y, [computeAverageProb(n, depth+1) for n in node[1:3]])



@memoize
def optimalBinaryTreeRecurse(arr,lb, rb):
	if(lb == rb): 
		return tuple([arr[lb], None, None])

	minTree = None
	minCost = float("inf")

	for root in range(lb,rb+1):
		#compute min right subtree
		right = None
		rightCost = float("inf")
		for k in range(root+1, rb+1): #i+1 to rightBound
			rc = optimalBinaryTreeRecurse(arr, root+1, rb) #right candidate
			rcCost = computeAverageProb(rc)
			if( rcCost < rightCost):
				right = rc 
				rightCost = rcCost

		#compute min left subtree
		left = None
		leftCost = float("inf")
		for k in range(lb, root): #lb to root - 1
			lc = optimalBinaryTreeRecurse(arr, lb,root-1) #left candidate
			lcCost = computeAverageProb(lc)
			if( lcCost < leftCost):
				left = lc 
				leftCost = lcCost

		candidateCost = computeAverageProb((arr[root],left,right))
		if(candidateCost < minCost):
			minTree = (arr[root],left,right)
			minCost = candidateCost


	return tuple([arr[root], left, right])

def stringifyTree(node):
	if(node is None): return ""

	left = stringifyTree(node[1])
	right = stringifyTree(node[2])

	if(len(left) == 0 and len(right) == 0): return node[0][0]
	return node[0][0] + '(' + left + ',' + right + ')'


tests = [ [('Don', 3/8.0), ('Isabelle', 3/8.0), ('Ralph', 1/8.0), ('Wally', 1/8.0)],
			[('A', 0.1), ('B', 0.2), ('C', 0.4), ('D', 0.3)],
			[('A',1/7.0),('B',1/7.0),('C',1/7.0),('D',1/7.0),('E',1/7.0),('F',1/7.0),('G',1/7.0)]
 ]

for t in tests:
	optimalBinaryTreeRecurse(clear=True)
	result = optimalBinaryTreeRecurse(t,0,len(t)-1)
	print  computeAverageProb(result),  stringifyTree(result)
