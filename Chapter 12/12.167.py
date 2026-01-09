from collections import Counter;s=input();
for k,v in Counter(s).items():
    if v==2: print(k); break