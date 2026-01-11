exprs=['x>2 and y>3', 'x>1 or y>-2', 'x>=0 and y<5', 'x>3 or x<-1', 'x>3 and x<10', 'not (x>2)', 'not (x>0 and x<5)', '10<x<=20', '0<y<=4 and x<5']
print(*exprs, sep='\n')
