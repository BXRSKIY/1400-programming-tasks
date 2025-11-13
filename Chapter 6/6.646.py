n=input().strip()
digits=[int(ch) for ch in n]
mx=max(digits); mn=min(digits)
print(n.index(str(mx))+1, n.index(str(mn))+1)
print(n[::-1].index(str(mx))+1, n[::-1].index(str(mn))+1)
