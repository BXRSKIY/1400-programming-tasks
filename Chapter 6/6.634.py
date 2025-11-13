m=int(input())
n=int(input())
mn=m*n
res1=[]
res2=[]
x=m
while x<=mn:
    res1.append(x)
    x+=m
y=n
while y<=mn:
    res2.append(y)
    y+=n
print(*res1)
print(*res2)
