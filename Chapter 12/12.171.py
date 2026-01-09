from collections import Counter;a=input();b=input();c1=Counter(a);c2=Counter(b);out=[];seen=set()
for c in a+b:
    if c not in seen and c1.get(c,0)==1 and c2.get(c,0)==1:
        out.append(c); seen.add(c)
print(' '.join(out))