cnt=0
x=100
res=[]
while cnt<15:
    if x%19==0:
        res.append(x)
        cnt+=1
    x+=1
print(*res)
