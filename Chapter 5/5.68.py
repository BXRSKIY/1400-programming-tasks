a=int(input());b=int(input());
for i in range(a,b+1):
 s=sum(int(c) for c in str(i))
 if i%7==0 and s%7==0:
  print(i)
