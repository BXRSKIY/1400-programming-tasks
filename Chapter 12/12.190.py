# 12.190. Преобразовать каждое слово:
# a) заменить первую букву 'а' на 'о';
# б) удалить из слова все вхождения заданной буквы.
s = input().rstrip("\n")
ch = input().rstrip("\n")
words = s.split()
out = []
for w in words:
    if 'а' in w:
        w = w.replace('а', 'о', 1)
    w = w.replace(ch, '')
    out.append(w)
print(" ".join(out))
