# 12.151. Дан текст, в начале которого есть пробелы и в котором имеются цифры.
# Найти порядковый номер максимальной цифры, начиная счет с первого символа, не являющегося пробелом.
# Если максимальных цифр несколько — найти номер первой из них.
s = input().rstrip("\n")
start = 0
while start < len(s) and s[start] == " ":
    start += 1

max_digit = -1
pos = None  # 0-based in original string
for i in range(start, len(s)):
    ch = s[i]
    if ch.isdigit():
        d = int(ch)
        if d > max_digit:
            max_digit = d
            pos = i
# номер считаем с 1, но от start (первый непробельный символ — 1)
print((pos - start) + 1)
