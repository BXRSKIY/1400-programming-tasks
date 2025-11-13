n=input().strip()
digits=[int(ch) for ch in n]
s=sum(digits)
p=1
for d in digits:
    p*=d
even_count=len(digits)%2==0
four=len(n)==4
first=int(n[0])
same_ends=n[0]==n[-1]
print(s>10)
print(p<50)
print(even_count)
print(four)
print(first<=6)
print(same_ends)
print("first" if n[0]>n[-1] else "last" if n[-1]>n[0] else "equal")
