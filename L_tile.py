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
	return ltileRecurse(k, exclude, (0,0), 2**k)

def ltileRecurse(k, exclude, bl, size):
	if(size == 2):
		#base case (2x2)
	else:
		#divide
		states = []
		for dx in range(2):
			for dy in range(2):
				states.append(ltileRecurse(k,exclude, bl + (dx*size//2, dy*size//2), size//2))

		#conquer