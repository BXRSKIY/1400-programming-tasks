n=int(input());p=1
for i in range(1,n+1):
 if n%i==0:
  p*=i
print(p)
