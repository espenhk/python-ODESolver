Ts = 20
t1 = 50
T1 = 180
T0 = 200
h = float(T1 - T0)/(t1*(Ts - T0))

# T'(t) = -h*(T-Ts)
def f(T, t):
    return -h*(T-Ts)

import ODESolver
solver = ODESolver.RungeKutta4(f)
solver.set_initial_condition(T0)
import numpy as np
time_points = np.linspace(0, 60*60, 1001)

def terminate(T, t, step_no):
    # Most recently computed T value: T[step_no]
    if abs(T[step_no] - Ts) < 1:
        return True  # terminate time loop
    else:
        return False

T, t = solver.solve(time_points, terminate)
from matplotlib.pyplot import plot, show
plot(t, T)
show()
