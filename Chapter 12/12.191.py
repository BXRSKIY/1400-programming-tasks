# 12.191. В каждом слове предложения переставить первую и последнюю буквы.
s = input().rstrip("\n")
words = s.split()
res = []
for w in words:
    if len(w) > 1:
        w = w[-1] + w[1:-1] + w[0]
    res.append(w)
print(" ".join(res))
