from ODESolver import ODESolver
import numpy as np
from numpy import exp
from scitools.std import plot, legend, hold

class RungeKutta2(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        u_new = u[k] + K2
        return u_new
        
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
        solver = RungeKutta2(rhs)
        solver.set_initial_condition(u0)
        time_points = np.linspace(0, xmax, n)
        u, t = solver.solve(time_points)
        plot(t, u)
        hold('on')
        legend_list.append('RK2 %d steps' % n)
    plot(exact_x, exact(exact_x))
    legend_list.append('exact: e^2x')
    legend(legend_list)
    hold('off')
    
if __name__ == '__main__':
    test_RungeKutta2()