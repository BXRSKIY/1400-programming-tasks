# 12.129. Дано слово, оканчивающееся символом '_'. Вставить заданную букву после буквы с заданным номером.
s = input().rstrip("\n")
k = int(input())
ch = input().rstrip("\n")
c = ch[0] if ch else ""
lst = list(s)
for i in range(len(lst)-1, k, -1):
    lst[i] = lst[i-1]
lst[k] = c
print("".join(lst))
