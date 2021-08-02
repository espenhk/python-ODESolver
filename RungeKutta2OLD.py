# Exercise E.22
from ODESolver import *
from scitools.std import *
import time

class RungeKutta2(ODESolver):
	def advance(self):
		u, f, k, t = self.u, self.f, self.k, self.t
		dt = t[k+1] - t[k]
		K1 = dt*f(u[k], t[k])
		K2 = dt*f(u[k] + 0.5*K1, t[k] + dt/2.)
		u_new = u[k] + (K2)
		return u_new
    	

if __name__ == "__main__":
	v0 = 5.
	g = 9.81
	x0 = 2.

	def rhs(u, t):
		return v0 - g*t
	
	def exact(t, x0):
		return x0 + v0*t - (1./2.)*g*t**2
	
	t = linspace(0,2,1001)
	solver = RungeKutta2(rhs)
	solver.set_initial_condition(x0)

	u, t = solver.solve(t)

	u_exact = exact(t, x0)

	plot(t, u, legend="Approx.")
	hold("on")
	time.sleep(2)
	plot(t, u_exact, legend="Exact")
