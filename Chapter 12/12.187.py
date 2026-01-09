# 12.187. Напечатать все слова предложения, которые встречаются в нем по одному разу.
s = input().rstrip("\n")
words = s.split()
from collections import Counter
c = Counter(words)
print(" ".join(w for w in words if c[w] == 1))
