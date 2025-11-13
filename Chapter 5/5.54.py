a=int(input());b=int(input());k=int(input());
for i in range(a,b+1):
 cnt=sum(1 for d in range(1,i+1) if i%d==0)
 if cnt==k:
  print(i)
