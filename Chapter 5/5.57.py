a=int(input());b=int(input());
for i in range(a,b+1):
 s=sum(d for d in range(1,i) if i%d==0)
 if s>i:
  print(i)
