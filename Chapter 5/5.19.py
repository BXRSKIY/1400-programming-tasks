import math
x=0.1
while x<=1.5+1e-9:
 print(round(math.sin(x),10))
 x=round(x+0.1,10)
