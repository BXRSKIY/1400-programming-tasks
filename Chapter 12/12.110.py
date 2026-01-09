# 12.110. Дано слово. Поменять местами его m-ю и n-ю буквы (нумерация с 1).
s = input().rstrip("\n")
m, n = map(int, input().split())
lst = list(s)
i, j = m-1, n-1
lst[i], lst[j] = lst[j], lst[i]
print("".join(lst))
