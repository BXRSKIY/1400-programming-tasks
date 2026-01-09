a=input();b=input();B=set(b);seen=set();out=[]
for c in a:
    if c not in seen:
        seen.add(c); out.append('да' if c in B else 'нет')
print(' '.join(out))