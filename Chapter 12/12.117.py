# 12.117. Дано слово.
# a) удалить третью букву;
# б) удалить k-ю букву.
# Удаление по правилам задач 12.116–12.124: сдвиг влево + '_' в конец.
word = input().rstrip("\n")
k = int(input())
a = word
if len(a) >= 3:
    a = a[:2] + a[3:] + "_"
else:
    a = a
b = word
b = (b[:k-1] + b[k:] + "_") if 1 <= k <= len(b) else b
print(a)
print(b)
