# TicTech
This is the directory for the TicTech use case.

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
**Decision variables**
* x_1	equals 1 if consulting is chosen, 0 otherwise
* x_2	equals 1 if off-the-shelf software is chosen, 0 otherwise
* x_3	equals 1 if purpose-built apps are chosen, 0 otherwise

**Constraints**

Exactly one technology must be chosen:

x_1+x_2+x_3=1.

**Objective**

max 12x_1 + 17x_2 + 25x_3

**Final formulation**
<pre>
max 12x_1 + 17x_2 + 25x_3
s.t.    x_1 + x_2 + x_3 = 1
        x_1, x_2, x_3 in {0,1}.
</pre>
