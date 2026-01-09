# 12.193. В каждом слове предложения заменить последнюю букву на первую.
s = input().rstrip("\n")
words = s.split()
res = []
for w in words:
    if w:
        res.append(w[:-1] + w[0])
print(" ".join(res))
