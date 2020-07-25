# TicTech

This is the directory for the TicTech use case.

It this is your first time visiting Learning MIP 
at Mip Master, you may want to start from the 
[homepage](https://mip-master.github.io/learning_mip/).

## Concepts covered
- The three steps to solve a problem
- The three components of a formulation
- Modeling with binary decision variables
- Calling a MIP solver
    
## Problem statement
The purpose of this use case is to illustrate
how to implement a **very simple** optimization
model. Therefore, the statement of the problem is 
very simple:
 
TicTech is an organization that needs to decide 
on the right type of technology to support 
them making complex decisions as their business grow.

TicTech has three options: <br>
1)	Consulting services <br>
2)	Off-the-shelf software <br>
3)	Purpose-built web applications (Apps)

Each technology has a score:
12-Consulting, 17-Software, 25-Apps.

The goal is to pick the technology with the highest 
score (which, of course, is app).

## Formulation
A typical formulation has three main components:
*	Decision variables
*	Constraints
*	Objective function

#### Decision variables

While there might be multiples ways to define the decision 
variables, choosing a good set of variables is crucial. 
Because, once the variables are defined, constraints and 
the objective are defined as functions of it.
For this problem, we defined three binary variables.

>*Decision variables*
>* `x_1`	equals 1 if consulting is chosen, 0 otherwise
>* $x_2$	equals 1 if off-the-shelf software is chosen, 0 otherwise
>* \\(x_3\\)	equals 1 if purpose-built apps are chosen, 0 otherwise

#### Constraints

In this use case, there is only one requirement: one, 
and only one, technology must be chosen.
We can formulated this requirement using a single constraint.

>Constraints – Exactly one technology:<br>
><pre>x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> = 1</pre>.

#### Objective

The objective of this problem is to maximize the score, which Mr. Mip formulated as following.

>Objective:<br>
><pre>max 12x<sub>1</sub> + 17x<sub>2</sub> + 25x<sub>3</sub></pre>

#### Final formulation

Putting all together, We arrive at the following formulation.

>Final formulation:
><pre>
>max 12x<sub>1</sub> + 17x<sub>2</sub> + 25x<sub>3</sub>
>s.t.    x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> = 1
>        x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub> in {0,1}.
></pre>
