"""
Newton's method of successive root approximation.
Made for HW #1 due 10/15/2014
"""

def isFunction(*functions):
	return reduce(lambda x,y: x and y, [hasattr(f, "__call__") for f in functions])

def derivative(f):
    def compute(x, dx):
        return (f(x+dx) - f(x))/dx
    return compute

def newton(f, guess, dx = 0.0000001, tolerance = 0.0000001):
	if( not isFunction(f)): 
		print "f must be callable."
		return float("inf")

	return iterateNewton(f,derivative(f), guess, dx, tolerance)

#stack overflow
def recurseNewton(f, df, approx, dx, tolerance):
	nApprox = (approx) - (f(approx)/df(approx, dx))

	if abs(nApprox - approx) <= tolerance: return nApprox
	return recurseNewton(f,df, approx, dx, tolerance)

def iterateNewton(f, df, approx, dx, tolerance):

	nApprox = (approx) - (f(approx)/df(approx, dx))

	while(abs(nApprox - approx) > tolerance):
		approx = nApprox
		nApprox = (approx) - (f(approx)/df(approx, dx))

	return nApprox


import math

a = lambda x: (float(x)/(1e3 * math.log(x,2))) - 1
b = lambda x: ((1e8 * float(x) * math.log(x,2)) / (100 * x * x)) - 1
c = lambda n: ((float(2**n))/(1e7 * n * n * n)) - 1

print "#1: ", newton(a, 1000)
print "#2: ", newton(b, 1000)
print "#3: ", newton(c, 1000)

