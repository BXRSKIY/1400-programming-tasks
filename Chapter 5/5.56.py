a=int(input());b=int(input());
mn=10**9;mnn=a
for i in range(a,b+1):
 cnt=sum(1 for d in range(1,i+1) if i%d==0)
 if cnt<mn:
  mn=cnt;mnn=i
print(mnn,mn)
