# 12.35. Дано слово из четного числа букв. Поменять местами его половины.
s = input().rstrip("\n")
n = len(s)
half = n // 2
print(s[half:] + s[:half])
