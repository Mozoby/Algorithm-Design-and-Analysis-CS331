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
	print colors
	return ltileRecurse(k, exclude, [0,0], 2**k, colors)

def ltileRecurse(k, exclude, bl, size, colors):
	if size == 2:
		color = colors.pop()
		print color
		return [ [color if (exclude[0] - bl[0] != i or exclude[1] - bl[1] != j) else None for j in range(2) ] for i in range(2)]
	else:
		tState = []
		#gather sub states
		for dy in range(2):
			for dx in range(2):
				nBl = (bl[0] + (dx*size//2), bl[1] + (dy*size//2))
				tExclude = exclude
				#Define the empty node
				if(exclude[0] - nBl[0] < size//2 and exclude[1] - nBl[1] < size//2):
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
				print "recurse", dx, dy
				tState.append(ltileRecurse(k, tExclude, nBl, size//2, colors))

		#Construct This 2D Array from subArrays
		arr = [[None] * size]*size
		for index, subArr in enumerate(tState):
			tBl = (index % 2, index//2)
			for y,row in enumerate(subArr):
				for x, value in enumerate(row):
					arr[tBl[1] + y][tBl[0] + x] = value

		#Fill in the missing pieces
		tColor = colors.pop()
		print tColor
		for y, row in enumerate(arr):
			for x, value in enumerate(row):
				if(value is None and ((exclude[0] - bl[0]) == x or (exclude[1] - bl[1]) == y)):
						#fill with color
						arr[y][x] = tColor

		return arr

print ltile(4, [15,15])







