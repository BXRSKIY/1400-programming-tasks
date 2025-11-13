n=input().strip()
m=int(input())
t=n[-m:] if m<=len(n) else n
summ=sum(int(ch) for ch in t)
print(summ)
