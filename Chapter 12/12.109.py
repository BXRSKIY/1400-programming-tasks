# 12.109. Дано слово. Поменять местами его третью и последнюю буквы.
s = input().rstrip("\n")
lst = list(s)
lst[2], lst[-1] = lst[-1], lst[2]
print("".join(lst))
