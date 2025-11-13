res=[]
x=1
while x<100:
    if x%13==0:
        res.append(x)
    x+=1
print(*res)
