"""
This is the most basic implementation of Marketing Budget Optimization named as call_to_action.

This version uses Gurobi as a solver.

Created by Rohit Karvekar (Jul 14, 21) for MipMaster.org.
"""

# import packages
import gurobipy as grb
import pandas as pd
import matplotlib.pyplot as plt

# declare data
channel_list = ["Print", "TV", "SEO", "SocialM"]
roi_perc = {"Print": 16, "TV": 9, "SEO": 6, "SocialM": 14}
penetration = {"Print": 2.1, "TV": 2.5, "SEO": 3.0, "SocialM": 0.9}
budget = 1_000_000
viewers_tgt = 1_500_000

# declare & initialize model
opt_model = grb.Model(name="Marketing Budget Optimization")

# decision variables
x_vars = opt_model.addVars(channel_list, vtype=grb.GRB.CONTINUOUS, lb=0, name="channels")

# constraints
opt_model.addConstr(sum(x_vars[i] for i in channel_list) <= budget, name="Total Budget")
opt_model.addConstr(sum(x_vars[i] for i in ["Print", "TV"]) >= 0.4 * budget, name="Conv Budget")
opt_model.addConstr(x_vars["Print"] <= 100_000, name="Print Min")
opt_model.addConstr(x_vars["SocialM"] <= 3 * x_vars["SEO"], name="SocialM Vs SEO")
opt_model.addConstr(sum(x_vars[i] * penetration[i] for i in channel_list) >= viewers_tgt,
                    name="Viewers Target")

# define objective function
opt_model.setObjective(sum(x_vars[i] * roi_perc[i] / 100 for i in channel_list))
opt_model.ModelSense = grb.GRB.MAXIMIZE
opt_model.setParam("MIPGap", 0.01)
opt_model.optimize()

opt_model.write('Marketing_Budget_Optimization.lp')

# extract optimization output
print(f"The Optimal Objective Value {opt_model.objVal}")

opt_df = pd.DataFrame.from_dict(x_vars, orient="index", columns=["Variable Object"])
opt_df.reset_index(inplace=True)
opt_df.rename(columns={"index": "Channel"}, inplace=True)
opt_df["Budget Allocated"] = opt_df["Variable Object"].apply(lambda item: item.X)
print(opt_df[["Channel", "Budget Allocated"]])

# visualize the output
plt.bar(opt_df["Channel"], opt_df["Budget Allocated"])
plt.xlabel("Channel")
plt.ylabel("Budget Allocated ($)")
plt.ylim(top=500000)
plt.title("Marketing Budget Optimization")
plt.tight_layout()
plt.show()

# Validate Model
# 1. Coefficients of Objective function -
obj_coeffs = opt_model.getAttr('Obj', x_vars)
print("obj_coeffs", obj_coeffs)

# 2. Constraint Expression
A = opt_model.getA()
plt.spy(A)
plt.show()

conv_budget_ct = opt_model.getConstrByName("Viewers Target")
row = opt_model.getRow(conv_budget_ct)
expression = str(row).replace('<gurobi.LinExpr:', '').replace('>', '')
print(f"Constraint Expression {expression} {conv_budget_ct.Sense} {conv_budget_ct.RHS}")
print(f"Constraint Value {row.getValue()}")

for ct in opt_model.getConstrs():
    row = opt_model.getRow(ct)
    LinExpr = str(row).replace('<gurobi.LinExpr:', '').replace('>', '')
    print(f"{ct.ConstrName} | {LinExpr} {ct.Sense} {ct.RHS} | Value {row.getValue()}")

# -------------------End of code-----------------------#

