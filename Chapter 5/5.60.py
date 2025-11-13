a=int(input());b=int(input());
for i in range(a,b+1):
 if str(i)[-1] in '02468' and i%3==0:
  print(i)
