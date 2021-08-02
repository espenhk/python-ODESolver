# Exercise E.23
from ODESolver import ForwardEuler, RungeKutta4
from numpy import sqrt
from scitools.std import plot, hold, savefig, legend
import numpy as np

'''
Information from exercise:
dy / dx = y' = 1/(2(y-1))
y(0) = y0 = 1 + sqrt(eps), eps = 0.001
x in [0, 4]
'''

eps = 0.001

def y(y, x):
    return float(1)/(2*(y-1))

def exact(x, eps=eps):
    return 1 + sqrt(x + eps)
    
def solve_plot_method(methodname):
    '''
    Designed for use with the ODESolver module.
    Takes in a methodname for solving an ODE, and starts by solving it with
    4 steps on the interval [0, 4]. It then doubles the amount of steps until
    the greatest error in the approximation is less than the given tolerance
    (in this case 0.5). I think 0.5 is an alright tolerance, as anything lower
    than this appears to give a "thread error" due to too many plots in one
    window.
    Function could be generalized to take in x_min, x_max, tol values etc.,
    but saw no need for that for this application.
    '''
    legend_list = []    # list of legends for plot, added at the end
    y0 = 1 + sqrt(eps)  # initial condition
    tol = 0.5
    steps = 4
    x_min = 0
    x_max = 4
    exact_array = np.linspace(x_min, x_max, 101)
    err = tol+1    # any value greater than tol, to be reassigned
    while abs(err) > tol:
        sol = methodname(y)
        sol.set_initial_condition(y0)
        x_array = np.linspace(x_min, x_max, steps+1) # steps+1 = points
        sol.solve(x_array)  # adds attributes t and u to sol
        plot(sol.t, sol.u)  # plot based on these attributes
        legend_list.append(str(methodname).split('.')[1] + 
                           (' %d steps' % steps))
        hold('on')
        for i in range(len(sol.u)):
            exact_u = exact(x_array[i])
            u = sol.u[i]
            curr_err = abs(exact_u - u)
            if i == 0:  # set first err
                err = curr_err
            elif curr_err > err:   
                err = curr_err # set err to greatest value of curr_err
        steps *= 2
    legend_list.append('exact solution')
    plot(exact_array, exact(exact_array))   # plot exact solution
    legend(legend_list) # add legend to plot
    savefig('%s.png' % methodname) # save plots to file, for later access
    hold('off') # make sure any new calls to method are in new window

solve_plot_method(ForwardEuler) # use method for ForwardEuler and RungeKutta4
solve_plot_method(RungeKutta4)

'''
Plots for this program can be accessed as 'ODESolver.ForwardEuler.png' and
'ODESolver.RungeKutta4.png', respectively.
Please note that not only does RungeKutta4 approximate "well enough" in fewer
steps, it also misses by a lot less in few steps (note y-axis).
'''