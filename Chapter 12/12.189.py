# 12.189. В предложении только два слова одинаковых. Найти эти слова.
s = input().rstrip("\n")
words = s.split()
from collections import Counter
c = Counter(words)
for w, k in c.items():
    if k == 2:
        print(w)
        break
