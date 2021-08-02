# Exercise 9.11
from Diff import Diff, Backward1
from numpy import allclose, zeros, exp

class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return ((f(x - 2*h) - 4*f(x - h) + 3*f(x))/(2*h))

def g(t):   # function used to create class instances
    return exp(-t)
    
def g_diff(t):  # exact derivative of function g
    return -exp(-t)
    
line = '|%36s|' % ('-'*36) # line for use in formatting
t = 0
max_k = 14
print line
print '|%10s|%12s|%12s|' % (' ', 'B1 - exact', 'B2 - exact')
print line
'''
The following loop assigns the h value according to the k value,
creates class instances of classes Backward1 and 2, assigns the value
of the differentiated at point t to variables, calculates the difference
between the approximation (computed) and the exact value, and prints
this difference in a formatted table.
'''
for k in range(max_k+1): # last value of k is max_k
    h = 2**(-k)
    back1 = Backward1(g, h) # create class instances
    back2 = Backward2(g, h)
    back1_eval = back1(t) # use call methods
    back2_eval = back2(t)
    diff1 = abs(back1_eval-g_diff(t))   # calculate difference from exact val
    diff2 = abs(back2_eval-g_diff(t))
    print '|h=%8.6f|%12.8f|%12.8f|' % (h, diff1, diff2)
print line
'''
Terminal> python Backward2.py 
|------------------------------------|
|          |  B1 - exact|  B2 - exact|
|------------------------------------|
|h=1.000000|  0.71828183|  0.75796439|
|h=0.500000|  0.29744254|  0.12339675|
|h=0.250000|  0.13610167|  0.02523921|
|h=0.125000|  0.06518762|  0.00572642|
|h=0.062500|  0.03191134|  0.00136494|
|h=0.031250|  0.01578904|  0.00033326|
|h=0.015625|  0.00785335|  0.00008234|
|h=0.007812|  0.00391644|  0.00002046|
|h=0.003906|  0.00195567|  0.00000510|
|h=0.001953|  0.00097720|  0.00000127|
|h=0.000977|  0.00048844|  0.00000032|
|h=0.000488|  0.00024418|  0.00000008|
|h=0.000244|  0.00012208|  0.00000002|
|h=0.000122|  0.00006104|  0.00000000|
|h=0.000061|  0.00003052|  0.00000000|
|------------------------------------|
'''

# We can observe that the Backward2 method is a lot better than
# the Backward1 method, reaching more than 8 digits accuracy in the
# time Backward1 reaches only 4 digits accuracy.