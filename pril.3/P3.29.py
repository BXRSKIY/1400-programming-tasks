exprs=['X%2!=0 and Y%2!=0', '((X<20)+(Y<20))==1', 'X==0 or Y==0', 'X<0 and Y<0 and Z<0', '((X%5==0)+(Y%5==0)+(Z%5==0))==1', 'X>100 or Y>100 or Z>100']
print(*exprs, sep='\n')
