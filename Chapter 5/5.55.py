a=int(input());b=int(input());
mx=-1;mxn=a
for i in range(a,b+1):
 cnt=sum(1 for d in range(1,i+1) if i%d==0)
 if cnt>mx:
  mx=cnt;mxn=i
print(mxn,mx)
