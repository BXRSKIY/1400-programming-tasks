# 12.118. Дано слово.
# a) удалить первую из букв 'о', если есть;
# б) удалить последнюю из букв 'л', если есть.
# Удаление: сдвиг влево + '_' в конец.
word = input().rstrip("\n")

a = word
pos = a.find("о")
if pos != -1:
    a = a[:pos] + a[pos+1:] + "_"

b = word
pos = b.rfind("л")
if pos != -1:
    b = b[:pos] + b[pos+1:] + "_"

print(a)
print(b)
