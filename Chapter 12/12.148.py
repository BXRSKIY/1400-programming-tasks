# 12.148. Дан текст. Напечатать все имеющиеся в нем цифры.
s = input().rstrip("\n")
digits = "".join(ch for ch in s if ch.isdigit())
print(digits)
