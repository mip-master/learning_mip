# Ukulele-la♬-la♫
This is the directory for the Ukulelelala (read Ukulele-la♬-la♫) 
use case.

It this is your first time visiting Learning MIP 
at Mip Master, you may want to start from the 
[homepage](https://mip-master.github.io/learning_mip/).

## Concepts covered
- Modeling with integer decision variables
- Summation notation
- If-then constraints
- Big-M constraints
- Complement of a binary variable
- LP files


## Problem statement
Ted runs a business on the music industry, a ukulele factory. 
His brand, Ukulelelala, is becoming a big success because 
of the great quality of the ukulele he produces and 
because of a recent marketing investment that Ted has made.

Every week, Ted ships all his production to seven major 
partner retailers. However, recently, the demand has been 
increasing tremendously to the point that Ted has not 
been able to keep up with production. 
Since Ted is not allowed to increase prices due to 
contractual reasons, every week he must decide how much 
to fulfil of each order he receives.

The table below shows the data from last week, when the 
factory was able to produce and ship 650 ukuleles, 510 
below the total demand which was 1,160.

<table>
<thead>
<tr>
<th>Retailer ID</th> <th>Wholesale Unit Price ($)</th>
<th>Order Qty.</th> <th>Shipped Qty.</th>
</tr>
</thead>
<tbody>
<tr> <td>R01</td> <td>47.00</td> <td>230</td> <td>50</td> </tr>
<tr> <td>R02</td> <td>65.00</td> <td>150</td> <td>135</td> </tr>
<tr> <td>R03</td> <td>70.00</td> <td>270</td> <td>270</td> </tr>
<tr> <td>R04</td> <td>68.00</td> <td>90</td> <td>90</td> </tr> 
<tr> <td>R05</td> <td>46.00</td> <td>190</td> <td>0</td> </tr>
<tr> <td>R06</td> <td>78.00</td> <td>55</td> <td>55</td> </tr>
<tr> <td>R07</td> <td>55.00</td> <td>120</td> <td>50</td> </tr>
</tbody>
</table>

Ted has a contract signed with each retailer. And one 
of the agreements is that Ted incurs a 
fee of 20 times the wholesale price of a ukulele if 
he can’t ship at least 50 ukuleles to a retailer that 
placed an order for that week.

Now, Ted needs to decide which retailer to ship to, and for
each retailer that he decide to serve that week, how
many ukuleles to ship.
The objective is to maximize profit, i.e., revenue 
minus penalty.

An optimal solution is given in the *Shipped Qty.* column
of the table above.

## Formulation
Let’s go through the three main steps that it typically 
takes to write a formulation.

#### Decision variables
The trick to define decision variables is to think about 
the unknowns of the problem.

For example, the number of ukuleles available for shipment 
is known, 650 in this case.
Likewise, the price by which he will sell to each retailer 
is also known, it’s given in the Wholesale Unit Price column.

Which retailers should Ted ship to? That’s unknown, 
it needs to be decided.
Once Ted decide to ship to a retailer, how many units 
should he ship? This is also to be determined.
Following this reasoning, we defined two set of decision 
variables.

>Decision variables:
>*  `x_i`	equal `1` if Ted ships to retailer `i`, `0` otherwise, 
    for all `i = R01, R02, …, R07`.
>*  `y_i`	the number of ukuleles shipped to retailer `i`, 
    for all `i = R01, R02, …, R07`.

Notice that `x` are binary variables (they can only take 
0-1 values) while `y` are integer variables. It wouldn’t 
make sense to define `y` as continuous since it doesn’t 
make sense to ship `50.3` ukuleles, for instance.

To simplify notation, let’s write `x_1, x_2, …, x_7` instead 
of `x_R01, x_R02, …, x_R07` when writing constraints and the 
objective function. Similarly, let’s write `y_1, y_2, …, y_7` 
instead of `y_R01, y_R02, …, y_R07`.

#### Constraints
Ideally, Ted would meet all order in full—because the more 
units he ships, the more profit he makes (we will model this 
with the objective function). This means that the optimization 
should try to increase each variable `y_i` as much as possible.

However, Ted doesn’t have enough supply. Therefore, we need 
to model the fact that the total shipped quantity cannot 
exceed `650` units.
>Constraints – Max availability:
><pre>y_1 + y_2 + y_3 + y_4 + y_5 + y_6 + y_7 ≤ 650.</pre>
Using summation notation, this is the same as the following:
∑_(i=1)^7y_i ≤650.
