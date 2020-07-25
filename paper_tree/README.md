# Paper Tree
This is the directory for the Paper Tree use case.

It this is your first time visiting Learning MIP 
at Mip Master, you may want to start from the 
[homepage](https://mip-master.github.io/learning_mip/).

## Problem statement
Paper Tree is well-known for producing paper and other 
materials, such as lumber, wood ships, and pulpwood, 
which are all derived from the tree that they harvest.

The company is committed to invest in technology to 
improve their operations and wants to start from the 
production planning. 

The flow chart gives the big picture of the first 
problem to be solved (more complex versions to come 
which will involve time periods and inventory).

![alt text](https://github.com/mip-master/learning_mip/blob/master/paper_tree/flowchart.png?raw=true)

Specifically, harvested trees are preprocessed in 
the land field. Larger-diameter logs yield sawtimber 
(also called saw logs) that go to the sawmill. 
Smaller-diameter logs and branches yield pulpwood 
and are routed to the pulpwood mill.
 
Three commodities come out of the sawmill: lumber, 
shavings, and dust. There is also a small fraction 
that results in bark, which is just waste and doesn’t 
have any value. All production of lumber goes to the 
marketplace. Shavings and dust can either go to the 
marketplace or to the linerboard mill, where it’s used 
for production of paper.

All the pulpwood that goes to the pulpwood mill 
becomes chips, except for a small fraction that 
results in bark. Chips can either go to the marketplace 
or to the linerboard mill for paper production.

All the paper from the linerboard mill go to the 
marketplace.

Ultimately, Paper Tree must decide how much timber 
and pulpwood to harvest, and how much shavings, and 
dust to use for paper production as to meet the demand 
of each commodity in the marketplace while maximizing 
its profit and without violating capacities.

There are tree capacity constraints, one for each mill, 
which says that input cannot exceed the processing 
capacity of the mill.

Excess demand in the marketplace is allowed only for 
dust, shavings, and lumber. For chips and paper, demand 
must be met exactly.

Finally, there are processing and inventory cost.

The input data is provided in the inputs folder.


