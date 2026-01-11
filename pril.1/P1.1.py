import math
exprs=['2*x', 'math.sin(x)', 'a**2', 'math.sqrt(x)', 'abs(n)', '5*math.cos(y)', '9.5*a**2', '3*math.sqrt(x)', 'math.sin(alpha)*math.cos(beta)+math.cos(alpha)*math.sin(beta)', 'a*math.sqrt(2*b)', '4*math.sin(2*alpha)*math.cos(beta)', '-5*math.sqrt(x+math.sqrt(y))']
print(*exprs, sep='\n')
