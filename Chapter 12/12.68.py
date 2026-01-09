# 12.68. Дано предложение. Определить, сколько в нем гласных букв.
s = input().rstrip("\n").lower()
vowels = set("аеёиоуыэюя")
print(sum(1 for ch in s if ch in vowels))
