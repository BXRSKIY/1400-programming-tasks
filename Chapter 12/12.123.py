# 12.123. Дано слово. Удалить из него все повторяющиеся буквы, оставив первые вхождения
# (в слове должны остаться только различные буквы).
# Удаление: сдвиг влево + '_' в конец (по числу удалённых символов).
s = input().rstrip("\n")
seen = set()
out = []
removed = 0
for ch in s:
    if ch in seen:
        removed += 1
    else:
        seen.add(ch)
        out.append(ch)
print("".join(out) + "_" * removed)
