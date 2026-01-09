# 12.73. Дан текст. Верно ли, что в нем есть пять идущих подряд одинаковых символов?
s = input().rstrip("\n")
ok = False
if len(s) >= 5:
    run = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            run += 1
            if run >= 5:
                ok = True
                break
        else:
            run = 1
print("да" if ok else "нет")
