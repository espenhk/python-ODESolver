# Exercise E.13
from ODESolver import RungeKutta4
import numpy as np
from numpy import exp
from scitools.std import plot, hold

# a
class Problem:
    '''
    I find the exercise text a bit vague on whether you should take in h as
    a parameter upon creating the class instance and then calculate a new h,
    or wait until the estimate_h method is called. I have interpreted it to
    be the latter, and thus no h is given as an attribute upon creating a
    class instance.
    Note that this means usage is dependent upon calling the estimate_h method
    before using the __call__ method.
    '''
    def __init__(self, Ts, T0, dt):
        self.Ts = Ts
        self.T0 = T0
        self.dt = dt
        
    def estimate_h(self, t1, T1):
        T0 = self.T0
        Ts = self.Ts
        h = (float(T1 - T0)/(t1*(Ts - T0)))
        self.h = h
        
    def __call__(self, T, t):
        return -self.h*(T - self.Ts)
        
    def terminate(self, T, t, step_no):
        Ts = self.Ts
        # Most recently computed T value: T[step_no]
        if abs(T[step_no] - Ts) < 1:
            return True  # terminate time loop
        else:
            return False

# b
def equal(a, b, tol=1e-9):
    '''
    A standard function to test for equality. Note that I have used 1e-9
    as opposed to a more conventional tolerance of 1e-14 because we are
    operating with fairly large numbers, so it would be wise to give some
    more headroom in terms of the tolerance for measuring equality.
    '''
    success = abs(a - b) < tol
    return success

def exact(x):
    return 180*exp((-x)/(450)) + 20

def test_Problem():
    '''
    Fairly straight forward test function as done in previous exercises.
    I use the case from E.12 as my test case.
    '''
    t0 = 0
    t1 = 50
    Ts = 20
    T0 = 200
    T1 = 180
    dt = t1 - t0
    inst = Problem(Ts, T0, dt)
    inst.estimate_h(t1, T1)
    # Analytical solution: h = (-20)/(-9000) = 1/450
    exact_h = (float(1)/(450))
    success_h = equal(inst.h, exact_h)
    assert success_h
    solver = RungeKutta4(inst)
    solver.set_initial_condition(T0)
    time_points = np.linspace(0, 60*60, 1001)
    u_calc, t_calc = solver.solve(time_points, inst.terminate)
    final_t = t_calc[-1] # value at which solution is terminated
    t_exact = np.linspace(t0, final_t, 1001)
    u_exact = exact(t_exact)
    plot(t_calc, u_calc, t_exact, u_exact, legend=['calculated', 'exact'])
    hold('on')
    # I will consider solutions adequate if first and last values are equal.
    success_u0 = equal(u_calc[0], u_exact[0])
    success_uT = equal(u_calc[-1], u_exact[-1])
    assert success_u0
    assert success_uT
    if (success_h and success_u0 and success_uT):
        print 'The test ran successfully!'
    hold('off') # in case of other plots

# c
'''
Advantages: we can store information about a practical problem, and have
several different methods for f.ex. estimating h (as in this case) or other
applicable functions that relate to the problem. As all problem information
and methods is contained in the class, we can easily see what's what in the
program.
Disadvantages: a lot of code and "difficult" implementation for simple problems.
'''

if __name__ == '__main__':
    test_Problem()

    # d
    # using h and dt from test case
    t0 = 0
    t1 = 50
    dt = t1 - t0
    T1 = 180
    Ts_list = [15, 22, 30]
    T0_list = [250, 200]
    for T0 in T0_list:
        for Ts in Ts_list:
            inst = Problem(Ts, T0, dt)
            inst.estimate_h(t1, T1)
            solver = RungeKutta4(inst)
            solver.set_initial_condition(T0)
            time_points = np.linspace(0, 60*60, 1001)
            u, t = solver.solve(time_points, inst.terminate)
            plot(t, u, legend=['Ts = %d, T0 = %d' % (Ts, T0)])
            hold('on')
        hold('off')
    
'''
Terminal> python pizza_cooling2.py 
The test ran successfully!
'''