n=int(input());x=float(input());s=0
fact=1
for k in range(0,n+1):
 if k>0:
  fact*=2*k*(2*k-1)
 s+=((-1)**k)*x**(2*k)/fact
print(round(s,10))
