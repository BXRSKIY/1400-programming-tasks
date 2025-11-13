a=int(input());b=int(input());
for i in range(a,b+1):
 print(i, sum(d for d in range(1,i+1) if i%d==0))
