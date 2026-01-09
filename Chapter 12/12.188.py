# 12.188. Напечатать все различные слова предложения.
s = input().rstrip("\n")
words = s.split()
seen = set()
out = []
for w in words:
    if w not in seen:
        seen.add(w)
        out.append(w)
print(" ".join(out))
