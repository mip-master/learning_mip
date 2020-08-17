"""
This is the most basic implementation of the Ukulelelala (read Ukulele-la-la) formulation.

This version uses PuLP as a modeling language and CBC as a solver.

Created by Aster Santana (Aug 16, 20), MipMaster.org.
"""

import pulp

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
mdl = pulp.LpProblem('Ukulele-la-la', sense=pulp.LpMaximize)

# Add variables
x = pulp.LpVariable.dicts(indexs=I, cat=pulp.LpBinary, name='x')
y = pulp.LpVariable.dicts(indexs=I, cat=pulp.LpInteger, name='y')

# Add Constraints
mdl.addConstraint(pulp.lpSum(y) <= PU, name='max_avty')
for i in I:
    mdl.addConstraint(SL * x[i] <= y[i], name=f'at_least_{i}')
    mdl.addConstraint(y[i] <= d[i] * x[i], name=f'at_most_{i}')

# Set the objective function
revenue = sum(p[i] * y[i] for i in I)
penalty = sum((PN * p[i]) * (1 - x[i]) for i in I)
mdl.setObjective(revenue - penalty)

# Optimize
mdl.solve()

# Retrieve the solution
y_sol = {i: int(y[i].value()) for i in I}
print(f'y = {y_sol}')
print(f'revenue: {revenue.value()}')
print(f'penalty: {penalty.value()}')
