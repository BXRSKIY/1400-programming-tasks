n=input().strip()
a=sum(1 for ch in n if ch=='3')
last=n[-1]
b=sum(1 for ch in n if ch==last)
c=sum(1 for ch in n if int(ch)%2==0)
s=sum(int(ch) for ch in n if int(ch)>5)
p=1
for ch in n:
    d=int(ch)
    if d>7:
        p*=d
print(a)
print(b)
print(c)
print(s)
print(p if p!=1 else 0)
print(n.count('0')+n.count('5'))
