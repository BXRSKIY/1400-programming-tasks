# 12.120. Дано предложение. Удалить символы с n1-го по n2-й (n1 <= n2).
# Удаление: сдвиг влево + '_' в конец (на каждый удаленный символ). Нумерация с 1.
s = input().rstrip("\n")
n1, n2 = map(int, input().split())
i = n1 - 1
j = n2 - 1
if not s:
    print(s)
else:
    i = max(0, i)
    j = min(len(s)-1, j)
    if i > j:
        print(s)
    else:
        removed = j - i + 1
        print(s[:i] + s[j+1:] + "_"*removed)
