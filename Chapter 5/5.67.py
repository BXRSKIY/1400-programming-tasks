a=int(input());b=int(input());
for i in range(a,b+1):
 if len(str(i))==2 and (int(str(i)[0])**2+int(str(i)[1])**2)%13==0:
  print(i)
