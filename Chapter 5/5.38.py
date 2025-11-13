n=int(input());x=float(input());s=0
fact=1
for k in range(0,n+1):
 if k>0:
  fact*=k
 s+=x**k/fact
print(round(s,10))
