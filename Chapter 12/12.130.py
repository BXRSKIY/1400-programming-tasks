# 12.130. Дано слово, оканчивающееся символом '_'. Вставить заданную букву после первой буквы 'и'.
s = input().rstrip("\n")
ch = input().rstrip("\n")
c = ch[0] if ch else ""
pos = s.find("и")
lst = list(s)
if pos == -1:
    print(s)
else:
    k = pos + 1  # вставляем после pos => индекс pos+1
    for i in range(len(lst)-1, k, -1):
        lst[i] = lst[i-1]
    lst[k] = c
    print("".join(lst))
