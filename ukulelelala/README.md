# Ukulele-la♬-la♫
This is the directory for the Ukulelelala (read Ukulele-la♬-la♫) 
use case.

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

An optimal solution is given in the Shipped Qty. column
of the table above.


