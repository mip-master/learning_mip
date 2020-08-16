"""
This is the most basic implementation of the Ukulelelala (read Ukulele-la-la) formulation.

This version uses CPLEX as a solver.

Created by Aster Santana (Aug 16, 20), MipMaster.org.
"""

from docplex.mp.model import Model

# Input Data
# retailers
I = [1, 2, 3, 4, 5, 6, 7]
# price
p = {1: 47, 2: 65, 3: 70, 4: 68, 5: 46, 6: 78, 7: 55}
# demand
d = {1: 230, 2: 150, 3: 270, 4: 90, 5: 190, 6: 55, 7: 120}
# production upper bound
PU = 650
# shipment lower bound
SL = 50
# penalty (num. of units)
PN = 20

# Define the model
mdl = Model('Ukulele-la-la')

# Add variables
x = mdl.var_dict(keys=I, vartype=mdl.binary_vartype, name='x')
y = mdl.var_dict(keys=I, vartype=mdl.integer_vartype, name='y')

# Add Constraints
mdl.add_constraint(mdl.sum(y) <= PU, ctname='max_avty')
mdl.add_constraints((SL * x[i] <= y[i] for i in I), names='at_least')
mdl.add_constraints((y[i] <= d[i] * x[i] for i in I), names='at_most')

# Set the objective function
revenue = sum(p[i] * y[i] for i in I)
penalty = sum((PN * p[i]) * (1 - x[i]) for i in I)
mdl.maximize(revenue - penalty)

# Optimize
mdl.solve()

# Retrieve the solution
y_sol = {i: int(y[i].solution_value) for i in I}
print(f'y = {y_sol}')
print(f'revenue: {revenue.solution_value}')
print(f'penalty: {penalty.solution_value}')
