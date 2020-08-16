"""
This is the most basic implementation of the TicTech formulation:

max 12*x_1 + 17*x_2 + 25*x_3
s.t.    x_1 + x_2 + x_3 = 1
        x_1, x_2, x_3 in {0, 1}

This version uses PuLP as a modeling language and CBC as a solver.

Created by Aster Santana (Aug 16, 20), MipMaster.org.
"""

import pulp

# Define the model
mdl = pulp.LpProblem('TicTech', sense=pulp.LpMaximize)

# Add variables
x = pulp.LpVariable.dicts(indexs=[1, 2, 3], cat=pulp.LpBinary, name='x')

# Add Constraints
mdl.addConstraint(x[1] + x[2] + x[3] == 1, name='exactly_one_tech')

# Set the objective function
mdl.setObjective(12 * x[1] + 17 * x[2] + 25 * x[3])

# Optimize
mdl.solve()

# Retrieve the solution
x_sol = {i: x[i].value() for i in [1, 2, 3]}
print(f'x = {x_sol}')
