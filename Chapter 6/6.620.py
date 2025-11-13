n=int(input())
s=str(n)
summ=0
prod=1
for ch in s:
    d=int(ch)
    summ+=d
    prod*=d
cnt=len(s)
avg=summ/cnt
sq=sum(int(ch)**2 for ch in s)
cu=sum(int(ch)**3 for ch in s)
first=int(s[0])
last=int(s[-1])
print(summ)
print(cnt)
print(prod)
print(avg)
print(sq)
print(cu)
print(first)
print(first+last)
