# 12.145. Дано слово из 12 букв. Переставить буквы: 1,12,2,11,...,6,7.
s = input().rstrip("\n")
n = len(s)
res = []
for i in range(n//2):
    res.append(s[i])
    res.append(s[n-1-i])
print("".join(res))
