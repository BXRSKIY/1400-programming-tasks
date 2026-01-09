# 12.49. Дано предложение. Напечатать все его буквы 'и'.
s = input().rstrip("\n")
res = "".join(ch for ch in s if ch == "и")
print(res)
