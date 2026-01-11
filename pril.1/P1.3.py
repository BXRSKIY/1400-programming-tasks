exprs=['a/(b*c)', 'a + b/c', '(a+b)/c', 'a*b/(c+2)', '(a/b)*((c-3)/d)', '(a/3 + b/2)/(b + c/(2+b))']
print(*exprs, sep='\n')
