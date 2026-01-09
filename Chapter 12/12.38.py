# 12.38. Дано слово. Перенести первые k его букв в конец.
s = input().rstrip("\n")
k = int(input())
k %= len(s) if s else 1
print(s[k:] + s[:k])
