k=int(input());found=0;i=2
while found<k:
 prime=True
 for d in range(2,int(i**0.5)+1):
  if i%d==0:
   prime=False;break
 if prime:
  print(i);found+=1
 i+=1
