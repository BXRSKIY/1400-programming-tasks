n=input().strip()
first=n[0]
print(sum(1 for ch in n if ch==first))
