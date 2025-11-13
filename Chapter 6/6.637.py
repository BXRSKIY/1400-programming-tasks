n=input().strip()[::-1]
pos=0
ans=0
for i,ch in enumerate(n, start=1):
    if ch=='8':
        ans=i
print(ans)
