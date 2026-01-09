# 12.131. Дано предложение, оканчивающееся символом '_'. Вставить заданную букву перед последней буквой 'и'.
s = input().rstrip("\n")
ch = input().rstrip("\n")
c = ch[0] if ch else ""
pos = s.rfind("и")
lst = list(s)
if pos == -1:
    print(s)
else:
    k = pos  # вставка перед pos => после (pos-1), т.е. на индекс pos
    for i in range(len(lst)-1, k, -1):
        lst[i] = lst[i-1]
    lst[k] = c
    print("".join(lst))
