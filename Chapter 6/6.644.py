n=input().strip()
digits=[int(ch) for ch in n]
mx=max(digits); mn=min(digits)
print( (mx-mn)%2==0 )
