"""
This is the most basic implementation of MarketUp formulation.

This version uses PuLP as a modeling language and CBC as a solver.

Created by Rohit Karvekar (Jul 14, 21) for MipMaster.org.
"""

import pulp

# Input Data
# marketing channels
mc = {1: 'Print', 2: 'TV', 3: 'SEO', 4: 'Social Media'}
I = list(mc)
# expected ROI
r = {1: 0.16, 2: 0.09, 3: 0.06, 4: 0.14}
# expected market penetration
p = {1: 2.1, 2: 2.5, 3: 3.0, 4: 0.9}
# total budget
tb = 1_000_000
# print budget
pb = 100_000
# viewer target
vt = 1_500_000
# minimum conventional channel allocation
ca = 0.4

# Define the model
mdl = pulp.LpProblem('market_up', sense=pulp.LpMaximize)

# Add variables
x = pulp.LpVariable.dicts(indexs=I, cat=pulp.LpContinuous, name='x')

# Add Constraints
# can't exceed the total budget
mdl.addConstraint(pulp.lpSum(x) <= tb, name='tb')
# minimum allocation to conventional channels
mdl.addConstraint(pulp.lpSum(x[i] for i in [1, 2]) >= ca * tb, name='ca')
# can't exceed the print budget
mdl.addConstraint(x[1] <= pb, name='pb')
# Social Media investment must be at most three times SEO investment
mdl.addConstraint(x[4] <= 3 * x[3], name='sm_seo')
# reach minimum viewers target
mdl.addConstraint(pulp.lpSum(p[i] * x[i] for i in I) >= vt, name='vt')

# Set the objective function
total_roi = pulp.lpSum(r[i] * x[i] for i in I)
mdl.setObjective(total_roi)

# Optimize
mdl.solve()

# Retrieve the solution
x_sol = {mc[i]: int(x[i].value()) for i in I}
print(f'Total ROI: {total_roi.value()}')
print(f'Optimal budget allocation: {x_sol}')

