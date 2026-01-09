# 12.50. Дано предложение. Напечатать «столбиком» все вхождения заданного символа.
s = input().rstrip("\n")
ch = input().rstrip("\n")
target = ch[0] if ch else ""
for c in s:
    if c == target:
        print(c)
