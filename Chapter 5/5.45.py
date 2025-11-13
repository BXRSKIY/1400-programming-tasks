a=int(input());b=int(input());k=int(input());s=0
for i in range(a,b+1):
 if i%k==0:
  s+=i
print(s)
