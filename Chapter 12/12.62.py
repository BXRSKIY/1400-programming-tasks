# 12.62. Дано предложение. Определить, сколько в нем одинаковых соседних букв.
# Считаем количество позиций i, где s[i] == s[i+1] и оба символа — буквы.
s = input().rstrip("\n")
cnt = 0
for i in range(len(s) - 1):
    if s[i].isalpha() and s[i+1].isalpha() and s[i] == s[i+1]:
        cnt += 1
print(cnt)
