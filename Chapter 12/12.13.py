# 12.13. Дано слово. Вывести k-й символ (k считается с 1).
s = input().rstrip("\n")
k = int(input())
print(s[k - 1])
