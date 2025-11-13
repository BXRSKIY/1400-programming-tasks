n=input().strip()
digits=[int(ch) for ch in n]
odds=[d for d in digits if d%2==1]
print(max(odds) if odds else -1)
mn=min(digits)
print(n.index(str(mn))+1)
