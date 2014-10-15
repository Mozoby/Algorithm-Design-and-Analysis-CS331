# CS331 HW Exercise 3
# Concept: After one quicksort partition you know that the pivot is in the correct place
# 	Looking at the pivot element's new index you can determine the position of proper element k
#	If the pivot is at an index less than k, then you know k is definitely to its right and vice versa
#	So you increment the next pivot value to one in the direction of k, and re-run the partition, repeat

import random

def sortedFind(k,a):
	b = sorted(a)
	return b[k]

def partition2(start, end, aaaa,a):
	il = start
	ir = end
	pElem = a[aaaa]
	nPivot = aaaa
	t=0

	while(il < ir):
		while(il < end and a[il] <= pElem):
			il += 1
		while(ir > start and a[ir] > pElem):
			ir -= 1

		if(il < ir):
			t = a[il]
			a[il] = a[ir]
			a[ir] = t
			if(il == nPivot): nPivot = ir
			if(ir == nPivot): nPivot = il
	a[nPivot] = a[ir]
	a[ir] = pElem
	nPivot = ir
	return nPivot

def partition(start, end, noPivot, parr):
	if(start == end): return start
	parr[noPivot], parr[end] = parr[end], parr[noPivot]
	stored=start
	for i in range(start,end):
		if(parr[i] < parr[end]):
			parr[i], parr[stored] = parr[stored], parr[i]
			stored += 1
	parr[stored], parr[end] = parr[end], parr[stored]
	return stored


def smartFind(k,a):
	pivot = len(a)//2
	leftBound = 0
	rightBound = len(a) - 1

	while(True):
		pPiv = pivot
		pPivElem = a[pivot]
		nPivot = partition2(leftBound, rightBound, pivot,a)
		if(nPivot < k):
			leftBound = nPivot + 1
			pivot = nPivot + 1
		elif(nPivot > k):
			rightBound = nPivot-1
			pivot = nPivot - 1
		else:
			pivot = nPivot
			break
	return a[pivot]

a = [random.randint(0,100) for x in range(1000)]
#print a
for x in range(len(a)):
	smart = smartFind(x,a)
	sort = sortedFind(x,a)
	if(smart != sort):
		print "DAMN", smart, sort, x

#print '\n'.join([reduce(lambda x,y: str(x==y), [smartFind(x,a), sortedFind(x,a)]) for x in range(len(a)) ])
#print a

