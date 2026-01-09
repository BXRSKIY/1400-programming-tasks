# 12.108. Дано слово. Поменять местами его вторую и пятую буквы.
s = input().rstrip("\n")
lst = list(s)
lst[1], lst[4] = lst[4], lst[1]
print("".join(lst))
