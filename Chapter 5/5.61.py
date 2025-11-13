a=int(input());b=int(input());
for i in range(a,b+1):
 s=sum(int(c) for c in str(i))
 if s%5==0:
  print(i)
