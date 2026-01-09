a=input();b=input();A=set(a);B=set(b);out=[]
for c in a:
    if c not in B: out.append(c)
for c in b:
    if c not in A: out.append(c)
print(' '.join(out))