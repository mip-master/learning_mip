# Paper Tree - Optimization Scripts
In this directory you will find multiple implementations 
of the optimization model for the Paper Tree use case.

## Directory guide
* `papertree_cplex.py` - The most basic implementation
    of the optimization model that uses CPLEX.
* `papertree_grb.py` - The most basic implementation
    of the optimization model that uses Gurobi.
* `papertree_pulp.py` - The most basic implementation
    of the optimization model that uses PuLP.
* `papertree_grb_pandas.py` - Same as `papertree_grb.py`
    except that the input data is loaded from csv files,
    instead of being hard-coded, and the solution is
    saved to a csv file, instead of being just printed.