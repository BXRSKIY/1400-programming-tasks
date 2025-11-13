n=int(input());cnt=0
for i in range(2,n+1):
 prime=True
 for d in range(2,int(i**0.5)+1):
  if i%d==0:
   prime=False;break
 if prime:
  cnt+=1
print(cnt)
