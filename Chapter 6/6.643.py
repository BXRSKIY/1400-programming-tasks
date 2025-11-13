n=input().strip()
digits=[int(ch) for ch in n]
mx=max(digits); mn=min(digits)
a=int(input())
print( (mx+mn)%a==0 )
