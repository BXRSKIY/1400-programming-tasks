n=input().strip()
digits=[int(ch) for ch in n]
mx=max(digits); mn=min(digits)
if n.index(str(mx))<n.index(str(mn)):
    print("max_left")
else:
    print("min_left")
