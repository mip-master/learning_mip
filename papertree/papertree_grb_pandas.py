"""
This is the implementation of the Paper Tree use case that reads the input data from csv files.

In the Input Data region, each input csv file is loaded into data frames which are then used to populate the
parameters dictionaries. Ideally, this data processing would be done in a separate module. The reason why we
do everything in this module is to avoid confusion for those learning Python.

This version uses Gurobi as a solver.

Created by Aster Santana (Aug 16, 20), MipMaster.org.
"""
import gurobipy as gp
import pandas as pd

# region Input Data
# load data into data frames
location_df = pd.read_csv('inputs/location.csv')
location_df = location_df.fillna(0)
commodity_df = pd.read_csv('inputs/commodity.csv')
commodity_df = commodity_df.fillna(0)
hauling_df = pd.read_csv('inputs/hauling_cost.csv')
output_ratio_df = pd.read_csv('inputs/output_ratio.csv')
# locations
I = dict([(i, v) for i, v in zip(location_df['Location ID'], location_df['Location'])])
# commodities
K = dict([(k, v) for k, v in zip(commodity_df['Commodity ID'], commodity_df['Commodity'])])
# processing cost
pc = dict([(i, v) for i, v in zip(location_df['Location ID'], location_df['Processing Cost ($/cu ft)'])])
# production upper bound/capacity
pu = dict([(i, v) for i, v in zip(location_df['Location ID'], location_df['Processing Capacity (cu ft)'])])
# hauling cost
hc = dict([((i, j, k), v) for i, j, k, v in zip(
    hauling_df['Origin ID'], hauling_df['Destination ID'], hauling_df['Commodity ID'],
    hauling_df['Hauling Cost ($/cu ft)'])])
# demand
d = dict([(k, v) for k, v in zip(commodity_df['Commodity ID'], commodity_df['Demand (cu ft)'])])
# market price
mp = dict([(k, v) for k, v in zip(commodity_df['Commodity ID'], commodity_df['Market Price ($/cu ft)'])])
# output ratio
r = dict([((k1, k2), v) for k1, k2, v in zip(
    output_ratio_df['Material ID'], output_ratio_df['Product ID'], output_ratio_df['Output Ratio'])])
# variables keys
x_keys = list(hc.keys())
# endregion

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
