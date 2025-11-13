n=input().strip()
digits=[int(ch) for ch in n]
mx=max(digits); mn=min(digits)
rev=n[::-1]
pos_end_mx=rev.index(str(mx))+1
pos_end_mn=rev.index(str(mn))+1
pos_start_mx=n.index(str(mx))+1
pos_start_mn=n.index(str(mn))+1
print(pos_end_mx, pos_start_mx)
print(pos_end_mn, pos_start_mn)
