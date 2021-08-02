# Exercise E.16
from math import log as ln
import numpy as np
from scitools.std import plot, hold
from math import exp
from ODESolver import RungeKutta4

u0 = 1

# a
class Decay:
    def __init__(self, a):
        self.a = a
        
    def __call__(self, u, t):
        return -self.a * u  # returns the differentiated of the function u
        
# b
a = ((float(ln(2)))/(5600)) # float-conversion used for clarity
inst = Decay(a) 

# c
dt = 500    # time step
T = 20000   # final t value
n = int(round(float(T)/dt)) + 1 # no of points (no of intervals = n-1)
t_array = np.linspace(0, T, n) # create array of time points

# Standard usage of ODESolver:
solver = RungeKutta4(inst)  # use inst.__call__ as function
solver.set_initial_condition(u0)
u, t = solver.solve(t_array)
plot(t, u)
hold('on')
final_calc = u[-1]
final_exact = exp(-a*T)
print 'Final calculated value: %.10f' % final_calc
print 'Final exact value: %.10f' % final_exact
print 'Difference in approximation: %.10f' % (final_calc - final_exact)
'''
Terminal>python radioactive_decay.py 
Final calculated value: 0.0841187888
Final exact value: 0.0841187620
Difference in approximation: 0.0000000268
'''