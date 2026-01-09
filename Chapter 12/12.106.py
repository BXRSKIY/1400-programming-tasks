# 12.106. Заменить в заданной строке все вхождения некоторой подстроки на другую подстроку.
# Ввод: строка s, затем old, затем new.
s = input().rstrip("\n")
old = input().rstrip("\n")
new = input().rstrip("\n")
print(s.replace(old, new))
