# Exercise E.30
from numpy import exp
import numpy as np
from scitools.std import plot, hold, legend

def RungeKutta2(f, U0, T, n):
    '''Solve u'=f(u,t), u(0)=U0, with n steps until t=T.'''
    t = np.zeros(n+1)
    u = np.zeros(n+1)
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        u[k+1] = u[k] + K2
    return u, t

def rhs(u, t):
    '''Right hand side of u' = 2u'''
    return 2*u
    
def exact(x):
    '''Analytical solution: u(x) = e^2x'''
    return exp(2*x)
    
def test_RungeKutta2():
    '''Test case: u' = 2u, u(0) = 1. '''
    legend_list = []
    u0 = 1
    xmax = 3
    exact_x = np.linspace(0, xmax, 1001)
    for n in [5, 10, 20, 100]:
        u, t = RungeKutta2(rhs, u0, xmax, n)
        plot(t, u)
        hold('on')
        legend_list.append('RK2 %d steps' % n)
    plot(exact_x, exact(exact_x))
    legend_list.append('exact: e^2x')
    legend(legend_list)
    hold('off')
    
test_RungeKutta2()

'''
Solution can be found as plot on screen when program is run. We observe
that as n increases, the approximation becomes closer and closer to the
exact solution. Already at 100 steps we have a very accurate approximation.
Note that increasing the number of steps over the same interval is
equivalent to reducing dt (the time step).
'''