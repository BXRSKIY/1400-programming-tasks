# 12.136. Дано слово. Переставить его первую букву на место k-й.
# При этом 2-я..k-я буквы сдвигаются влево на одну.
# Ввод: слово, затем k (1 <= k <= len).
s = input().rstrip("\n")
k = int(input())
if not s or k <= 1:
    print(s)
else:
    k = min(k, len(s))
    first = s[0]
    # удалить первую, вставить на позицию k (1-indexed) => индекс k-1 в новой строке длины len-1
    rest = s[1:]
    idx = k - 1
    print(rest[:idx-1] + first + rest[idx-1:] if idx-1 >= 0 else first + rest)
