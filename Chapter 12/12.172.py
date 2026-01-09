from collections import Counter;a=input();b=input();v=input();c1=Counter(a);c2=Counter(b)
ok = all(c in c1 for c in c2) if v=='1' else all(c1[c]>=c2[c] for c in c2)
print('да' if ok else 'нет')