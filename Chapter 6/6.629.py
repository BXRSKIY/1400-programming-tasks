cnt=0
x=100
res=[]
while cnt<10:
    if x%9==0 and x%10==7:
        res.append(x)
        cnt+=1
    x+=1
print(*res)
