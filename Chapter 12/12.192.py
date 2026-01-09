# 12.192. В каждом слове предложения удалить первую и последнюю буквы.
s = input().rstrip("\n")
words = s.split()
res = []
for w in words:
    if len(w) > 2:
        res.append(w[1:-1])
    else:
        res.append("")
print(" ".join(res))
