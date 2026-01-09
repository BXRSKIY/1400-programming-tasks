# 12.111. Дано слово из четного числа букв. Поменять местами: 1<->2, 3<->4, ...
s = input().rstrip("\n")
lst = list(s)
for i in range(0, len(lst), 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]
print("".join(lst))
