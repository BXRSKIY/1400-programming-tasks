x=int(input())
p=1
n=0
while p<x:
    n+=1
    p*=n
if p==x:
    print(n)
else:
    print(0)
