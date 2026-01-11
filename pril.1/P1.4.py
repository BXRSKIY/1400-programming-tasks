import math
exprs=['math.sqrt(x1**2 + x2**2)', 'x1*x2 + x1*x3 + x2*x3', 'v0*t + a*t**2/2', 'm*v**2/2 + m*g*h', '1/R1 + 1/R2', 'm*g*math.cos(alpha)', '2*math.pi*R', '(a*d + b*c)/(a*d)', 'gamma*m1*m2/r**2', 'b**2 - 4*a*c', 'I**2*R', 'a*b*math.sin(c)', 'math.sqrt(a**2 + b**2 - 2*a*b*math.cos(c))', '(math.sqrt(x+1)+math.sqrt(x-1))/(2*math.sqrt(x))', 'abs(x) + abs(x+1)', 'abs(1-abs(x))']
print(*exprs, sep='\n')
