n=int(input());x=float(input());s=0
for k in range(0,n+1):
 s+=((-1)**k)*x**k
print(s)
