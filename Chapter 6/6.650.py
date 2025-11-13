n=input().strip()
a=int(input())
b=int(input())
k=int(input())
m=int(input())
digits=[int(ch) for ch in n]
print(sum(digits)<a)
p=1
for d in digits: p*=d
print(p>b)
print(len(n)==k)
print(int(n[0])>m)
