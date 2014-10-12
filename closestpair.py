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
	arry = sorted(arr, key=lambda x: x[1])
	sortTime = time.clock() - sortTime
	print "Sort:",sortTime

	dist = c(arrx,arry, 0, len(arrx) - 1)
	print "Elevate:", dist[1]
	return sqrt(dist[0])

def elevate(arry, d, midXVale):
	md = d
	for i in range(len(arry)):
		if(arry[i][0] >= (midXVale-d) and arry[i][0] <= (midXVale+d)):
			maxy = arry[i][1] + d
			for j in range(i+1, len(arry)):
				if(arry[j][1] > maxy): break
				md = min(md, dist2(arry[i], arry[j]))
	return md

def c(arrx, arry, start, end):
	if(start == end): return (2000000000,0)
	if(end-start == 1): return (dist2(arrx[start], arrx[end]),0)

	mid = (start + end)//2

	m1 = c(arrx,arry, start, mid)
	m2 = c(arrx,arry, mid+1, end)

	d = min(m1[0],m2[0])
	elevateTime = time.clock()
	d = min(d, elevate(arry,d, arrx[mid][0]))
	elevateTime = time.clock() - elevateTime

	return (d,elevateTime + m1[1] + m2[1])

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
for i in range(5):
	points = set([(random.randint(0,100000), random.randint(0,100000)) for i in range(100)])
	points = list(points)
	goodTime = time.clock()
	goodAlgo = closestPair(points)
	goodTime = time.clock() - goodTime
	badTime = time.clock()
	badAlgo = brute(points)
	badTime = time.clock() - badTime

	print goodTime, badTime

