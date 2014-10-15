"""
L-Tile implementation across a 2D grid of size 2^k by 2^k.
From CS331 Class Discussion from 10/10/2014
Author: Bryan Thornbury
"""

# Input:
#	k ::= (int) Grid is of size 2^k
#	exclude ::= (tuple) (x,y) coords of excluded tile 
# Returns: (boolean) whether or not the tiling configuration can be completed

def ltile(k, exclude):
	colors = [i for i in range(4**k, 0, -1)]
	return ltileRecurse([[None for x in  range(2**k)] for y in range(2**k)], k, exclude, [0,0], 2**k, colors)


def printArr(tp):
	for row in tp:
		print '\t'.join(map(str, row))

def ltileRecurse(arr, k, exclude, bl, size, colors):
	#print size
	if size == 2:
		color = colors.pop()
		for rIndex, row in enumerate(arr[bl[1]:bl[1]+size]):
			#print rIndex, bl, row[bl[0]:bl[0] + size]
			for i in range(len(row[bl[0]:bl[0] + size])):
				if(exclude[0] != (bl[0] + i) or exclude[1] != (bl[1] + rIndex)):
					row[bl[0] + i] = color
				#else:
					#print 'excluded', exclude
		#printArr(arr)
		return arr
		#return [ [color if (exclude[0] - bl[0] != j or exclude[1] - bl[1] != i) else None for j in range(2) ] for i in range(2)]
	else:
		#gather sub states
		for dy in range(2):
			for dx in range(2):
				nBl = (bl[0] + (dx*size//2), bl[1] + (dy*size//2))
				tExclude = exclude
				#Define the empty node
				if( 0 < exclude[0] - nBl[0] < size//2 and  0 < exclude[1] - nBl[1] < size//2):
					print "don't change"
					tExclude = exclude #don't change it
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
				#print "recurse", dx, dy
				#print tExclude, nBl
				ltileRecurse(arr,k, tExclude, nBl, size//2, colors)
		#print arr

		#place extra tile
		color = colors.pop()
		for rIndex, row in enumerate(arr[bl[1]:bl[1]+size]):
			for i in range(len(row[bl[0]:bl[0] + size])):
				if (exclude[0] != (bl[0] + i) or exclude[1] != (bl[1] + rIndex)) and row[i] is None:
					row[bl[0] + i] = color

		return arr

		# #Construct This 2D Array from subArrays
		
		# printArr(arr)
		# #tState.reverse()
		# for index, subArr in enumerate(tState):
		# 	tBl = ((index % 2) * size//2, (index//2) *size//2 )
		# 	#print tBl
		# 	for y,row in enumerate(subArr):
		# 		for x, value in enumerate(row):
		# 			#print "(",tBl[1] + y, tBl[0] + x,")", value
		# 			arr[tBl[1] + y][tBl[0] + x] = value
		# printArr(arr)
		# #Fill in the missing pieces
		# tColor = colors.pop()
		# #print tColor
		# for y, row in enumerate(arr):
		# 	for x, value in enumerate(row):
		# 		if(value is None and ((exclude[0] - bl[0]) == x and (exclude[1] - bl[1]) == y)):
		# 			#fill with color
		# 			arr[y][x] = tColor
		# 		else:
		# 			arr[y][x] = value

		# return arr

tp = ltile(3, [7,7])
printArr(tp)
#tp.reverse()








