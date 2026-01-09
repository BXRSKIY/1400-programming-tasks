# 12.87. Даны два слова. Сколько начальных букв первого совпадает с начальными буквами второго?
w1 = input().rstrip("\n")
w2 = input().rstrip("\n")
m = min(len(w1), len(w2))
cnt = 0
for i in range(m):
    if w1[i] == w2[i]:
        cnt += 1
    else:
        break
print(cnt)
