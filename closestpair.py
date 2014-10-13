"""
Closest Pair Divide and Conquer Algorithm
From 10/10/2014 Class Discussion

Author: Bryan Thornbury
"""
from math import sqrt
def dist(p1, p2):
	return sqrt(pow((p1[0]-p2[0]),2) + pow((p1[1]-p2[1]), 2))

def dist2(p1,p2):
	return pow((p1[0]-p2[0]),2) + pow((p1[1]-p2[1]), 2)


# Arr ::= [(x1,y1), (x2,y2), ..., (xn, yn)]
def closestPair(arr):
	sortTime = time.clock()
	arrx = sorted(arr, key=lambda x: x[0])
	sortTime = time.clock() - sortTime
	#print "Sort:",sortTime

	dist = c(arrx, 0, len(arrx) - 1)
	#print "Elevate:", dist[1]
	return sqrt(dist)

def elevate(arry, d):
	md = d
	for i in range(len(arry)):
		maxy = arry[i][1] + md
		for j in range(i+1, len(arry)):
			if(arry[j][1] > maxy): break
			md = min(md, dist2(arry[i], arry[j]))
			maxy = arry[i][1] + md
	return md

def c(arrx, start, end):
	if(start == end): return 2000000000
	if(end-start == 1): return dist2(arrx[start], arrx[end])

	mid = (start + end)//2

	m1 = c(arrx, start, mid-1)
	m2 = c(arrx, mid+1, end)

	arry = sorted(arrx[start:end+1], key = lambda x: x[1])

	d = min(m1,m2)
	d = min(d, elevate(arry,d))

	return d

def brute(arr):
	md = 2000000000
	p = []
	for index,elem in enumerate(arr):
		for i in range(index+1, len(arr)):
			nd = dist2(elem,arr[i])
			if(nd < md): p = [elem,arr[i]]
			md = min(md, nd)
	return (sqrt(md), p)

import random, time
g = []
b = []
n = 1000
for i in range(5):
	points = set([(random.randint(0,100000)/10.0, random.randint(0,100000)/10.0) for i in range(n)])
	points = list(points)
	goodTime = time.clock()
	goodAlgo = closestPair(points)
	goodTime = time.clock() - goodTime
	badTime = time.clock()
	badAlgo = brute(points)
	badTime = time.clock() - badTime

	g.append(goodTime)
	b.append(badTime)
print "N =", n
print "D&C:", sum(g)/float(len(g))
print "Brute:", sum(b)/float(len(b))

