# 12.194. В каждом слове предложения удалить все буквы, кроме первой и последней.
s = input().rstrip("\n")
words = s.split()
res = []
for w in words:
    if len(w) > 1:
        res.append(w[0] + w[-1])
    else:
        res.append(w)
print(" ".join(res))
