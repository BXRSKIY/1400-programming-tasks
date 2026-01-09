# 12.195. В каждом слове предложения заменить все буквы, кроме первой и последней, символом '*'.
s = input().rstrip("\n")
words = s.split()
res = []
for w in words:
    if len(w) > 2:
        res.append(w[0] + "*"*(len(w)-2) + w[-1])
    else:
        res.append(w)
print(" ".join(res))
