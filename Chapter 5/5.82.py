for i in range(10,100):
 a=i//10;b=i%10
 if (a*a+b*b)%13==0:
  print(i)
for i in range(10,100):
 s=sum(int(c) for c in str(i))
 if i==s+s*s:
  print(i)
