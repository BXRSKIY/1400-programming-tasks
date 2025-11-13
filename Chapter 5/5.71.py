a=int(input());b=int(input());
for i in range(a,b+1):
 if i%10 in [2,4,8] and i%3==0:
  print(i)
