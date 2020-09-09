# Introduction

MIP stands for *Mixed-integer Programming*. 
It's an important field of mathematical optimization 
and a fantastic technology for modeling and solving 
decision-making problems in a variety of domains such 
as supply chain, logistics, scheduling,
electric power generation, and so many more.

Here, you will find lots of practical, hands-on examples to 
learn and apply MIP to solve real-world problems. Many years of
academic and
industry experience are being combined to develop this material
aiming to help you to adopt the best practices right from the 
beginning.

It's our commitment to keeping this material freely available
for everyone.

One of the primary goal of Mip Master is to make the MIP
technology accessible beyond the operations research community,
and especially to the data science community.
With that in mind, the use cases we share are designed to be
as didactic as they can be (without compromising performance)
and all of them are implemented in Python.

After covering this material, you will be able to:
1.	Identify when a problem can be modeled as a MIP
2.	Model a variety of problem using MIP
3.	Implement and solve MIP model using a MIP solver in Python

We will cover the basic theory, but the emphasis will be on 
application. In fact, first we teach you how to use MIP with 
lots of practical, hands-on examples. You will find templates 
and sample codes that you can personalize, expand, and use in 
your own projects. Then, as you feel 
motivated, we give you the opportunity to dive deeper into 
the theory and move to the next level.

While coding is an important component of this course, only 
basic Python skills are required. And if you are a beginner in 
Python, you will learn a lot more in this course as well.

We hope you will enjoy this content and find it useful.
We also hope that you will always come back to learn more 
and to use MIP with confidence, starting from your 
next project!

# Use Cases
If you want to jump straight to the use cases,
here is a list of the ones currently available.
Keep in mind that we are constantly adding new use cases
to the list.
We recommend to explore the use cases following the
order in this list, especially if you are not familiar with
MIP yet.

1.  **[TicTech](
    https://github.com/mip-master/learning_mip/tree/master/tictech
    )** - Illustrates how to implement a 
    *very simple* optimization model.<br>
    *Author: Aster Santana, Jul 2020*
    
    Concepts:
    - The three steps to solve a business problem
    - The three components of a mathematical formulation
    - Modeling with binary decision variables
    - Calling a MIP solver

2.  **[Ukulele-la♬-la♫](
    https://github.com/mip-master/learning_mip/tree/master/ukulelelala
    )** - A simplified version of a practical
    fulfillment problem.<br>
    *Author: Aster Santana, Jul 2020*
    
    Concepts:
    - Integer decision variables
    - Summation notation
    - If-then constraints
    - Big-M constraints
    - Complement of a binary variable
    - LP files
    
3.  **[Paper Tree](
    https://github.com/mip-master/learning_mip/tree/master/paper_tree
    )** - A simplified version of a practical 
    production planning.<br>
    *Author: Aster Santana, Jul 2020*
    
    Concepts:
    - Network flow problem
    - Conservation of flow constraint
    - Optimization data model

Would you like to contribute with an use case too?!
We provide [templates](
https://github.com/mip-master/learning_mip/tree/master/templates
) and would be happy to helping you to build your use case!

# The MIP Technology
Let's dive a little deeper into the MIP technology.

## What is MIP?
MIP stands for Mixed-Integer Programming.
* “Programming” is synonyms for “Optimization”.
* “Integer” is for integer decision variables, 
which includes binary variables as a special case.
* “Mixed” is to indicate a mix of continuous and 
integer decision variables.

Putting all together,
**“MIP is an optimization problem that involves a mix 
of continuous and integer/binary decision variables.”**

If you are not familiar with optimization, no worries! 
We will provide more background throughout the use cases.
For now, all you need to know is that an optimization 
problem consists of minimizing or maximizing an objective 
function subject to a set of constraints, and the 
objective and constraints are functions of 
decision variables.

A decision variable could be the number of 
products to manufacture in given machine,
or whether to fulfil orders from Facility A or from 
Facility B.
Examples of objectives include minimizing waste and 
maximizing profit.
A constraint could be a resource capacity such as 
maximum number of daily working hours.

At the end of the day, we want to define the set of 
all acceptable (feasible) solutions to the problem and 
identify one that has the best objective value. 

There are three major steps to that end:
1.	**Definition**: Understanding the business problem 
in detail, which includes identifying the main goals, 
data, and requirements.
2.	**Modeling**: Building a precise representation 
of the problem—In our case, first a mathematical 
formulation and then an optimization model that the 
computer can understand.
3.	**Solution**: Searching for the best solution—in 
our case using a MIP solver.

You will be surprised to see the variety of practical
problems that you can solve with what you will learn here!

Few more facts:
*	MIP is an extension of Linear Programming (LP), 
    which is the most basic class of optimization problems.
*	Sometimes we use the acronym MILP instead of MIP to 
    emphasize that the problem is *linear*, opposed to 
    *non-linear*.
*	Some people prefer the word “optimization” instead 
    of “programming”, in which case the acronym becomes MIO 
    or MILO.
*	Not every MIP is an optimization problem, in the sense that
    we are not always interested in minimizing/maximizing 
    something. In some cases, we just want to find a feasible 
    solution, i.e., a solution 
    that meet all requirements simultaneously. Puzzles, such as 
    Sudoku, are good examples of it.
*   There are many classes of optimization problems. 
    Classes can be defined, for example, based on modeling
    assumptions, such as deterministic or stochastic; type of 
    decision variables present in the model, such as
    continuous, integer, or both; or
    type of expressions defining the objective and
    constraints, such as linear, convex, non-convex.
    We will be dealing mostly
    with deterministic mixed-integer linear programs.


## Why MIP?
MIP is a powerful decision-making technology. 
And here are four features of MIP to support this claim: 
representativeness, robustness, tractability, optimality 
guarantee.

*	**Representativeness:**
The first step in solving and business problem using 
optimization is to write a precise mathematical formulation 
to the problem. This process is also called modeling—we 
will use this terminology very often.
Representativeness means that a broad class of 
business problems can be modeled using MIP.
*	**Robustness:**
Modeling, whether using MIP and any other technology, 
is not a trivial task.
And in the dynamic environment we live nowadays, 
business problems tend to change quite often.
As you will see in the use cases, MIP is very adaptable,
that’s what robustness means. To the most part, 
it is easy to extend or modify a MIP model to address 
new business requirements.
*	**Tractability:**
Modeling the business problem is only the first step. 
Eventually we need to solve the model.
As you might guess, the larger the number of variables 
and constraints, the harder it is to solve the model.
The good news is that practical models with *millions* 
of variables and constraints can often be solved efficiently.
Another good news is that the MIP solver will do all the 
hard work of solving the problem for you!
*	**Optimality guarantee:**
What does it mean to solve an optimization problem?
Usually it means finding THE best feasible solution 
with respect to an objective. It's easier to explain
with an example.
Suppose you use the gradient descent algorithm to fit 
a *non-linear* regression model to a data set. How do you 
know that the solution you found gives you the best fit?
The solution you get, depends on the starting point you 
choose.
So, unless your non-linear model has a special structure, 
you will never know for sure whether the solution you got is 
the best you can possibly have or not.
Solutions from a MIP solver, on the other hand, comes 
with an *optimality gap*—also called *MIP gap* or *duality gap*.
If the gap is zero, you know that no solution with 
better objective exists.
If the gap is greater than zero, you still have an upper bound on 
"how far" your solution is from optimality.

To recap, MIP is great because:
*	It’s applicable to a broad class or problems.
*	It’s very flexible and adaptable.
*	It can handle very large problems, with possibly 
    millions of variables and constraints.
*	The solution comes with an optimality gap 
    that tells you how close you may be from the best 
    possible solution.


## Why MIP now? 
To answers this question, let’s have a look at the history 
of MIP theory and MIP solvers.

First, MIP is not a new technology. Here is quote from the 
[book](
https://www.springer.com/gp/book/9783540682745
)
*50 Years of Integer Programming 1958-2008, From the Early 
Years to the State-of-the-Art*<br>
>“In 1958, Ralph E. Gomory transformed the field of integer 
programming when he published a short paper that described 
his cutting-plane algorithm for pure integer programs and 
announced that the method could be refined to give a finite 
algorithm for integer programming.”

MIP tractability used to be a concern in the beginning. 
However, there has been tremendous progress around 
solving MIP. Here is a quote from a recent [paper](
http://www.mit.edu/~dbertsim/papers/Machine%20Learning%20under%20a%20Modern%20Optimization%20Lens/Logistic%20Regression-From%20Art%20to%20Science.pdf
) 
by Dimitris Bertsimas and Angela King:<br>
>“In the period 1991–2015, algorithmic advances in 
Mixed-Integer Linear Optimization (MILO) coupled with 
hardware improvements have resulted in an astonishing 
450 billion factor speedup in solving MILO problems”

The number 450 billion is very impressive, isn’t it?
And this number continue to grow year after year as 
can be seen from improvement performance reports by 
commercial MIP solvers such as 
[CPLEX](
https://www.ibm.com/analytics/cplex-optimizer
) and 
[Gurobi](
https://www.gurobi.com/
).

For several decades, MIP has been transforming operation 
across industries, including [airlines crew scheduling](
https://www.isye.gatech.edu/news/airline-optimization-isye
), 
[sport scheduling](
http://www.sports-scheduling.com/in-the-news.html
), 
and the whole field of supply chain. 
However, mostly only those developing the MIP theory 
were using this technology for solving practical problems 
initially.
Deep understanding of the theoretical and computational 
aspects of MIP used to be required for modeling and solving 
real-world problems.

This reality began to change in the 90’s when the body 
of literature on how to model and solve MIP increased.
Around the same time, the commercial MIP solvers [Xpress](
https://en.wikipedia.org/wiki/FICO_Xpress
) and 
[CPLEX](
https://www.ibm.com/analytics/cplex-optimizer
)
began to gain popularity.
Few years later, in early 2000’s, two of the first open 
source MIP solvers, [GLPK](
https://en.wikipedia.org/wiki/GNU_Linear_Programming_Kit
) 
and [COIN-OR CBC](
https://en.wikipedia.org/wiki/COIN-OR#CBC
), 
were public released. Another big player in the commercial 
side, 
[Gurobi](
https://www.gurobi.com/
), was founded in 2008.

With that, a much broader community began to adopt MIP to solve 
challenging problem in various industries.
However, some specific modeling language, such as 
[GAMS](
https://en.wikipedia.org/wiki/General_Algebraic_Modeling_System
), 
[AMPL](
https://en.wikipedia.org/wiki/AMPL
), or 
[AIMMS](
https://en.wikipedia.org/wiki/AIMMS
), would 
still be required solving MIP. This used to somehow limit 
the usage of MIP to the Operations Research community.

Another wave of democratization of the MIP technology 
came with the broad adoption of Python as a programming 
language for data science and analytics.
Many Python interface for optimization packages, 
such as [Pyomo](
https://en.wikipedia.org/wiki/Pyomo
), 
[Mip](
https://pypi.org/project/mip/
), and 
[PuLP](
https://coin-or.github.io/pulp/
), emerged.
Gurobi, in particular, has put tremendous effort in making 
its optimization package easily accessible via [gurobipy](
https://www.gurobi.com/documentation/9.0/quickstart_mac/py_python_interface.html
), 
the Gurobi-Python interface, along with comprehensive, 
well-structured documentation. CPLEX has also taken a 
similar path.

Now, any data scientist (and other analytics 
professionals) can much more easily leverage 
MIP technology 
for solving all sort of combinatorial problems.
However, the myth that optimization is only for Operation 
Researchers still remains around.


## MIP for Data Scientists
Apart from the fact that MIP is a 
powerful technology on its own, and it’s accessible even 
by those outside of the Operations Research community, 
we claim that **the combination of data science and MIP is 
a powerful one**.

In many applications, part of the input data to MIP models 
comes from a data science team.
Perhaps the most classic example is demand data. Data 
scientists use forecasting to predict demand and then 
the output from the forecasting algorithm (point forecast) 
becomes input to the MIP model.
In this example, prediction and optimization are done in 
disconnected silos. we claim that this disconnection has 
created a gap between what we have been doing and what 
we could have been achieving with data analytics.

As an example, there has been a case where data scientists 
and operations researchers solved, 
in close collaboration, an important real-world problem in 
which they used MIP to discretize and 
maximize expected revenue over ten thousand probability 
curves generated by a machine learning algorithm.

Here is a quote from 
Ed Rothberg, the CEO of Gurobi, taken from a two-minutes [video](
https://www.youtube.com/watch?v=RDOsP-gUWgQ
):<br>
>“MIP complements other analytics techniques like machine 
learning quite nicely, we will see more and more companies 
building application that combines machine learning and 
optimization.”

In conclusion, there are big benefits in bringing MIP and data 
science (or machine learning) capabilities closer together.


## Is it hard to learn MIP?
This is a tricky question. And the answer highly depends 
on the level of expertise you want to achieve.
Compared to Machine Learning, it might be fair to say that:
*	MIP is harder to grasp than basic regression and 
classification techniques.
*	Deep learning and reinforcement learning, on the other 
hand, are more difficult to learn than MIP.

Notice that all these Machine Learning techniques are 
themselves application of optimization—and MIP is one 
kind of optimization.

For example, every time we try to fit a model to a data, 
we are searching for the parameters of the model that 
minimize error or maximize likelihood. So, this is an 
optimization problem, even though data scientists don’t 
typically see this way. Why don't they?
The answer is simple: when minimizing sum 
of square errors, there is a *closed form solution* for the 
best fitting parameters.  The formula buries the optimization.
Now, replace the linear model with an exponential model, 
as we would do to model the spreading of a contagious 
disease, for example.
In this case, there is no closed formula and we 
need to use some explicit optimization approach, like
a gradient descent algorithm.

Going back to the main question, there are several levels 
of expertise that one can achieve in optimization.
This includes being able to:
1.	**Admit** that a problem is an optimization problem 
    when an expert tells you so.
2.	**Recognize** when a problem can be formulated as 
    an optimization problem.
3.	**Model/Formulate** business problems as optimization 
    problems.
4.	**Solve** optimization problems using existing 
    solvers and algorithms.
5.	**Design** customized algorithms for solving 
    challenging optimization problems.
6.	**Develop** theory for solving whole classes of 
    optimization problems.
     
Level 3 is the one that requires most practice because 
there is not a single recipe for MIP modeling.
Level 4 is the most fun for most people. That’s when 
you hit the run button and follow the progress of
the optimization solver by watching its log, like this 
one (notice the MIP Gap going to zero in last column):

<pre>
         Nodes                                         Cuts/  
    Node  Left     Objective  IInf  Best Integer    Best Bou  nd    ItCnt     Gap
                                                              
 *     0+    0                       6.11449e+07   5.06574e+  07            17.15%
       0     0   5.45123e+07   284   6.11449e+07   5.45123e+  07     2230   10.85%
 *     0+    0                       5.75671e+07   5.45123e+  07             5.31%
 *     0+    0                       5.69224e+07   5.45123e+  07             4.23%
       0     0   5.45151e+07   284   5.69224e+07     Cuts: 2  48     2773    4.23%
 *     0+    0                       5.67861e+07   5.45151e+  07             4.00%
       0     0   5.45175e+07   284   5.67861e+07     Cuts: 2  43     3350    3.99%
       0     0   5.45176e+07   284   5.67861e+07     Cuts: 1  42     3823    3.99%
 *     0+    0                       5.59982e+07   5.45176e+  07             2.64%
       0     0   5.45178e+07   284   5.59982e+07     Cuts: 1  40     4397    2.64%
 *     0+    0                       5.53996e+07   5.45178e+  07             1.59%
 *     0+    0                       5.51997e+07   5.45182e+  07             1.23%
       0     0  -1.00000e+75     0   5.51997e+07   5.45182e+  07     4397    1.23%
 *     0+    0                       5.47518e+07   5.45182e+  07             0.43%
</pre>

At the beginning, you will spend a lot of time around 
Level 3 and Level 4, which is the main focus of the 
Learning MIP project. Level 6 is where you find Operations 
Research professionals who hold a Ph.D. degree.
Level 5 is also super fun, but require some more experience.
To get to Level 6, you need to deeply understand the 
theory underling Levels 3-5. We can point directions for 
those interested on that. But first we focus only on 
the theory that is needed to make you a *thoughtful practitioner*.


# Summary
Well done!
So far, you have already learned that:
*	MIP is a very powerful optimization-based technology 
    for decision-making.
*	MIP finds application in a variety of domains because 
    of its spectacular representativeness.
*	MIP is adaptable and flexible to easily address new 
    business requirements on the fly.
*	We can solve MIP instances with millions of variables 
    thanks to recent theoretical and computational advancements.
*	MIP technology is now accessible much beyond the 
    Operations Research community (thanks to commercial and 
    open-source MIP solvers), and that’s why you are here.
*	Most Machine Learning techniques are optimization-based 
    techniques.
*	This content will lead you to the right level of 
    expertise needed to solve real-world problems without 
    burning your time with unnecessary optimization theory.

# Next steps
We hope you are ready and excited to start your MIP journey!
Or move to the next level if MIP is not new to you.
 
Now it’s time to see practical examples and learn how to model 
and solve real-world optimization problems as a Mip Master!
We recommend you start from the [TicTech](
https://github.com/mip-master/learning_mip/tree/master/tictech
) use case.

## Meet Mr. Mip
Before you get started, let's introduce you to Mr. Mip,
our role model for learning and applying the MIP technology.
Mr. Mip is a consultant who is expert in using mathematical 
optimization and programming for solving decision-making 
problems. You will learn by observing Mr. Mip in action
throughout the use cases.
To take the most from this experience, you should focus on 
understanding how Mr. Mip thinks. He’s very systematic, 
so it will be easy to recognize his thinking pattern.

## Setting up a MIP Solver
You will need a solver to solve MIP models. 
A MIP solver is basically a professional implementation of a 
[branch and bound](
https://en.wikipedia.org/wiki/Branch_and_bound
) 
method combined with a 
[cutting-plane](
https://en.wikipedia.org/wiki/Cutting-plane_method
)
method.

While there are many solvers available for solving MIP, 
we list only four of the most traditional solvers 
(follow this [link](
https://en.wikipedia.org/wiki/List_of_optimization_software
) 
for a more comprehensive list of optimization software). 
All of them are proprietary solvers except for CBC, 
which is open-source and part of the [COIN-OR](
https://www.coin-or.org/
) 
project. Free academic licenses are available for all 
the three proprietary solvers listed below.

If you are beginning and eligible for an academic license, 
Gurobi has very friendly and well-structured documentation. 
If you are not eligible for an academic license, you may 
want to start with CBC-PuLP. The good news is that the 
modeling syntax of these solvers are all very similar, 
meaning that if you learn how to use one solver, then it's 
easy to switch to another solver.

* [CBC](
https://github.com/coin-or/Cbc
)
    - Type: Open source
    - Python interface: [PuLP](
    https://pypi.org/project/PuLP/
    ), 
    [Installation guide](
    https://coin-or.github.io/pulp/main/installing_pulp_at_home.html#installation
    )
* [CPLEX](
https://www.ibm.com/analytics/cplex-optimizer
)
    - Type: Proprietary
    - Python interface: [DOcplex](
    https://cdn.rawgit.com/IBMDecisionOptimization/docplex-doc/master/docs/index.html
    ),
    [Installation guide](
    https://cdn.rawgit.com/IBMDecisionOptimization/docplex-doc/master/docs/getting_started_python.html
    )
* [Gurobi](
https://www.gurobi.com/
)
    - Type: Proprietary
    - Python interface: [gurobipy](
    https://www.gurobi.com/documentation/9.0/quickstart_mac/py_python_interface.html
    ),
    [Installation guide](
    https://www.gurobi.com/documentation/9.0/quickstart_mac/ins_the_anaconda_python_di.html#section:Anaconda
    )
* [Xpress](
https://www.fico.com/en/products/fico-xpress-optimization
)
    - Type: Proprietary
    - Python interface: [xpress](
    https://pypi.org/project/xpress/
    ),
    [Installation guide](
    https://www.msi-jp.com/xpress/learning/square/01-python-interface.pdf
    )


# Philosophy

The goal of Mip Master with the Learning MIP project is
to democratize the MIP technology so it can be use
beyond the Operation Research community.

Traditionally, MIP had been thought by
starting with a comprehensive revision of the theory
underlying the MIP technology. Specifically, students would 
spend a lot of time learning Linear Algebra, geometry of
linear inequalities, the simplex algorithms, and so on.
Only then students would start learning formulation.
Implementation, the most fun part, tends to be the 
last component of traditional MIP-related courses.

We take a completely different approach. We focus
first on the application and introduce the theory 
along the way as necessary, only after building the 
motivation for it. In fact, we start
with formulation and implementation from the first
use case, because we know that the whole learning 
experience will be much more meaningful and enjoyable 
this way.

We believe that this is the right approach, even for
the Operation Research community, simply because
this is how human brain works. You see a problem,
you try to solve it with the tools you have available,
and if you are not satisfied with the result, you
go after more sophisticated tools. And by the time
you recognize that more complex tools are 
needed, you already have the motivation and clarity 
it takes to grasp that underling theory.
