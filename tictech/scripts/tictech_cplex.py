"""
This is the most basic implementation of the TicTech formulation:

max 12*x_1 + 17*x_2 + 25*x_3
s.t.    x_1 + x_2 + x_3 = 1
        x_1, x_2, x_3 in {0, 1}

This version uses CPLEX as a solver.

Created by Aster Santana (Aug 16, 20), MipMaster.org.
"""

import docplex.mp.model as cpl

# Define the model
mdl = cpl.Model('TicTech')

# Add variables
x = mdl.var_dict(keys=[1, 2, 3], vartype=mdl.binary_vartype, name='x')

# Add Constraints
mdl.add_constraint(x[1] + x[2] + x[3] == 1, ctname='exactly_one_tech')

# Set the objective function
mdl.maximize(12 * x[1] + 17 * x[2] + 25 * x[3])

# Optimize
mdl.solve()

# Retrieve the solution
x_sol = {i: x[i].solution_value for i in [1, 2, 3]}
print(f'x = {x_sol}')
