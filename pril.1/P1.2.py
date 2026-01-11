import math
exprs=['-1/x**2', 'a/(b*c)', '(a/b)*c', '(a+b)/2', '5.45*(a+2*b)/(2-b)', '(-b+math.sqrt(b**2-4*a*c))/(2*a)', '(-b+1/a)*c/2', '1/(1+(a+b)/2)', '1/(1+1/(2+1/(2+3/5)))', '2**(m**n)']
print(*exprs, sep='\n')
