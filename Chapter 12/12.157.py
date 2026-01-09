s=input();b=c=0
for x in s:
    if x.isdigit(): c+=1; b=max(b,c)
    else: c=0
print(b)