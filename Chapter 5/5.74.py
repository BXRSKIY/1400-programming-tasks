a=int(input());b=int(input());
for i in range(a,b+1):
 if i%9==0 and str(i)[-1]=='7':
  print(i)
