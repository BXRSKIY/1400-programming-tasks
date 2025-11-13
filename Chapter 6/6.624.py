n=input().strip()
sign=1
ans=0
for ch in n:
    d=int(ch)
    ans+=sign*d
    sign*=-1
print(ans)
