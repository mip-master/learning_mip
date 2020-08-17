"""
This is the most basic implementation of the TicTech formulation:

max 12*x_1 + 17*x_2 + 25*x_3
s.t.    x_1 + x_2 + x_3 = 1
        x_1, x_2, x_3 in {0, 1}

This version uses Gurobi as a solver.

Created by Aster Santana (May 31, 20), MipMaster.org.
"""

import gurobipy as gp

# Define the model
mdl = gp.Model('TicTech')

# Add variables
x = mdl.addVars([1, 2, 3], vtype=gp.GRB.BINARY, name='x')

# Add Constraints
mdl.addConstr(x[1] + x[2] + x[3] == 1, name='exactly_one_tech')

# Set the objective function
mdl.setObjective(12 * x[1] + 17 * x[2] + 25 * x[3], sense=gp.GRB.MAXIMIZE)

# Optimize
mdl.optimize()

# Retrieve the solution
x_sol = {i: x[i].X for i in [1, 2, 3]}
print(f'x = {x_sol}')
