a=int(input());b=int(input());
for i in range(a,b+1):
 if any(i%p==0 for p in [11,13,17,19]):
  print(i)
