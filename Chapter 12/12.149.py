# 12.149. Дан текст. Определить количество цифр в нем.
s = input().rstrip("\n")
print(sum(1 for ch in s if ch.isdigit()))
