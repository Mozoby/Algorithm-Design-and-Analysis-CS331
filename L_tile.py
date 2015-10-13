"""
L-Tile implementation across a 2D grid of size 2^k by 2^k.

Author: Bryan Thornbury
"""

# Input:
#	k ::= (int) Grid is of size 2^k
#	exclude ::= (tuple) (x,y) coords of excluded tile 
# Returns: (boolean) whether or not the tiling configuration can be completed

def ltile(k, ex):
	colors = [i for i in range(4**k, 0, -1)]
	return ltileRecurse([[None for x in  range(2**k)] for y in range(2**k)], k, ex, [0,0], 2**k, colors)

#prints the array neatly
def printArr(tp):
	tp = tp[:]
	tp.reverse()
	for row in tp:
		print '\t'.join(map(str, row))

#verifies every number appears exactly 3 times
def verifyArr(arr):
	count = dict()

	for row in arr:
		for value in row:
			if value is not None:
				if value in count:
					count[value] += 1
				else:
					count[value] = 1
	for key in count.keys():
		if count[key] != 3: 
			return False
	return True

def ltileRecurse(arr, k, exclude, bl, size, colors):
	if size == 2:
		color = colors.pop()
		for rIndex, row in enumerate(arr[bl[1]:bl[1]+size]):
			for i in range(len(row[bl[0]:bl[0] + size])):
				if(exclude[0] != (bl[0] + i) or exclude[1] != (bl[1] + rIndex)):
					row[bl[0] + i] = color
		return arr
	else:
		#gather sub states
		for dy in range(2):
			for dx in range(2):
				nBl = (bl[0] + (dx*size//2), bl[1] + (dy*size//2))
				tExclude = exclude[:]
				#Define the empty node
				if( 0 <= exclude[0] - nBl[0] < size//2 and  0 <= exclude[1] - nBl[1] < size//2):
					tExclude = exclude[:] #don't change it
				else:
					#change excluded to the inner
					if(dx == 0):
						tExclude[0] = nBl[0] + (size//2) - 1
					else:
						tExclude[0] = nBl[0]

					if(dy == 0):
						tExclude[1] = nBl[1] + (size//2) - 1
					else:
						tExclude[1] = nBl[1]

				ltileRecurse(arr,k, tExclude, nBl, size//2, colors)

		#Place extra tile
		color = colors.pop()
		for rIndex, row in enumerate(arr[bl[1]:bl[1]+size]):
			for i in range(len(row[bl[0]:bl[0] + size])):
				if (exclude[0] != (bl[0] + i) or exclude[1] != (bl[1] + rIndex)) and row[bl[0] + i] is None:
					row[bl[0] + i] = color
		return arr

good = True
for k in range(1,6):
	print k
	for i in xrange(2**k):
		for j in xrange(2**k):
			tp = ltile(k, [i,j])
			#printArr(tp)
			good = good and verifyArr(tp)
print "All Cases Verified:", good








