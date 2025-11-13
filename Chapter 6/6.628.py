cnt=0
x=500
res=[]
while cnt<20:
    if x%13==0 or x%17==0:
        res.append(x)
        cnt+=1
    x+=1
print(*res)
