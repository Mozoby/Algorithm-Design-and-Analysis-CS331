"""
QuickSelect - Use Quicksort partitioning for a faster selection algorithm.

https://en.wikipedia.org/wiki/Quickselect

Author: Bryan Thornbury
"""

import random

# Naive Selection. Sort the list and index k. a is the unsorted list.
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



def testAlgorithmCorrectness():
	a = [random.randint(0,100) for x in range(1000)]

	for x in range(len(a)):
		smart = smartFind(x,a)
		sort = sortedFind(x,a)

		if(smart != sort):
			return False

	return True


if __name__ == "__main__":
	print testAlgorithmCorrectness()
