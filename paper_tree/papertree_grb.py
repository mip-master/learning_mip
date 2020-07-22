"""
This is the implementation of the Paper Tree use case.

This version uses Gurobi as a solver.

Created by Aster Santana (Jul 11, 20), MipMaster.org.
"""
import gurobipy as gp

# Input Data
# locations
I = {1: 'Forest', 2: 'Pulpwood Mill', 3: 'Sawmill', 4: 'Linerboard Mill', 5: 'Marketplace'}
# commodities
K = {1: 'Pulpwood', 2: 'Sawtimber', 3: 'Chips', 4: 'Dust', 5: 'Shavings', 6: 'Lumber', 7: 'Paper', 8: 'Bark'}
# processing cost
pc = {1: 67.9, 2: 67.9, 3: 23.5, 4: 115.05, 5: 0.0}
# production upper bound/capacity
pu = {2: 230.0, 3: 270.0, 4: 120.0}
# hauling cost
hc = {(1, 2, 1): 45.0, (1, 3, 2): 24.0, (2, 4, 3): 13.45, (2, 5, 3): 64.0, (3, 4, 4): 11.8, (3, 4, 5): 11.8,
      (3, 5, 4): 75.0, (3, 5, 5): 75.0, (3, 5, 6): 62.5, (4, 5, 7): 44.05}
# demand
d = {3: 65, 4: 20, 5: 35, 6: 110, 7: 15}
# market price
mp = {3: 310, 4: 45, 5: 64, 6: 150, 7: 2860}
# output ratio
r = {(1, 3): 0.85, (1, 8): 0.15, (2, 4): 0.1, (2, 5): 0.15, (2, 6): 0.7, (2, 8): 0.05, (3, 7): 0.25, (3, 8): 0.75,
     (4, 7): 0.55, (4, 8): 0.45, (5, 7): 0.4, (5, 8): 0.6}
# variables keys
x_keys = list(hc.keys())

# Define the model
mdl = gp.Model('PaperTree')

# Add variables
x = mdl.addVars(x_keys, vtype=gp.GRB.CONTINUOUS, name='x')

# Add Constraints
# capacity
mdl.addConstr(x[1, 2, 1] <= pu[2], name='cap_pulpwood_mill')
mdl.addConstr(x[1, 3, 2] <= pu[3], name='cap_sawmill')
mdl.addConstr(x[2, 4, 3] + x[3, 4, 4] + x[3, 4, 5] <= pu[4], name='cap_linerboard_mill')
# demand
mdl.addConstr(x[2, 5, 3] == d[3], name='demand_chips')
mdl.addConstr(x[3, 5, 4] >= d[4], name='demand_dust')
mdl.addConstr(x[3, 5, 5] >= d[5], name='demand_shavings')
mdl.addConstr(x[3, 5, 6] >= d[6], name='demand_lumber')
mdl.addConstr(x[4, 5, 7] == d[7], name='demand_paper')
# flow balance
mdl.addConstr(r[1, 3] * x[1, 2, 1] == x[2, 4, 3] + x[2, 5, 3], name='flow_bal_chips')
mdl.addConstr(r[2, 4] * x[1, 3, 2] == x[3, 4, 4] + x[3, 5, 4], name='flow_bal_dust')
mdl.addConstr(r[2, 5] * x[1, 3, 2] == x[3, 4, 5] + x[3, 5, 5], name='flow_bal_shavings')
mdl.addConstr(r[2, 6] * x[1, 3, 2] == x[3, 5, 6], name='flow_bal_lumber')
mdl.addConstr(r[3, 7] * x[2, 4, 3] + r[4, 7] * x[3, 4, 4] + r[5, 7] * x[3, 4, 5] == x[4, 5, 7], name='flow_bal_paper')

# Set the objective function
revenue = sum(mp[k] * x[i, j, k] for (i, j, k) in x_keys if j == 5)
hauling_cost = sum(hc[key] * x[key] for key in x_keys)
processing_cost = pc[1] * (x[1, 2, 1] + x[1, 3, 2]) + pc[2] * x[1, 2, 1] + pc[3] * x[1, 3, 2] + \
                  pc[4] * (x[2, 4, 3] + x[3, 4, 4] + x[3, 4, 5])
mdl.setObjective(revenue - processing_cost - hauling_cost, sense=gp.GRB.MAXIMIZE)

# Optimize
mdl.optimize()

# Retrieve the solution
print(f'Total profit {mdl.objVal:.2f}')
for (i, j, k), v in x.items():
    print(f'From {I[i]:<15} to {I[j]:<15} {v.X:5.2f} {K[k]}')
