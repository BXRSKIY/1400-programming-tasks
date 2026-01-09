# 12.21. Дано слово. Получить часть, образованную буквами с m-й по n-ю (1-indexed, включительно).
s = input().rstrip("\n")
m, n = map(int, input().split())
print(s[m-1:n])
