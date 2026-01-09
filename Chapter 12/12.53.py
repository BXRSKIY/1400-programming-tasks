# 12.53. Дано предложение. Вывести «столбиком» все вхождения двух заданных символов.
s = input().rstrip("\n")
a = input().rstrip("\n")
b = input().rstrip("\n")
ca = a[0] if a else ""
cb = b[0] if b else ""
for ch in s:
    if ch == ca or ch == cb:
        print(ch)
