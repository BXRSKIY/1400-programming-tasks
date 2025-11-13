a=int(input());b=int(input());
for i in range(a,b+1):
 s=sum(int(c) for c in str(i))
 if i%s==0 if s!=0 else False:
  print(i)
