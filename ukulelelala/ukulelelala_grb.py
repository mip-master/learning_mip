"""
This is the most basic implementation of the Ukulelelala (read Ukulele-la-la) formulation.

This version uses Gurobi as a solver.

Created by Aster Santana (Jun 20, 20), MipMaster.org.
"""

import gurobipy as gp

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
mdl = gp.Model('Ukulele-la-la')

# Add variables
x = mdl.addVars(I, vtype=gp.GRB.BINARY, name='x')
y = mdl.addVars(I, vtype=gp.GRB.INTEGER, name='y')

# Add Constraints
mdl.addConstr(y.sum() <= PU, name='max_avty')
mdl.addConstrs((SL * x[i] <= y[i] for i in I), name='at_least')
mdl.addConstrs((y[i] <= d[i] * x[i] for i in I), name='at_most')

# Set the objective function
revenue = sum(p[i] * y[i] for i in I)
penalty = sum((PN * p[i]) * (1 - x[i]) for i in I)
mdl.setObjective(revenue - penalty, sense=gp.GRB.MAXIMIZE)

# Optimize
mdl.optimize()

# Retrieve the solution
y_sol = {i: int(y[i].X) for i in I}
print(f'y = {y_sol}')
print(f'revenue: {revenue.getValue()}')
print(f'penalty: {penalty.getValue()}')
