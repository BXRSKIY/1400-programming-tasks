a=int(input())
b=int(input())
aa=abs(a); bb=abs(b)
r=bb
while r>=aa:
    r-=aa
if b<0:
    r=-r
print(r)
