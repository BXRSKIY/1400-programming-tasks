# 12.146. Дана строка (только буквы). Заменить все буквы 'а' на 'б' и наоборот,
# как заглавные, так и строчные.
s = input().rstrip("\n")
out = []
for ch in s:
    if ch == "а":
        out.append("б")
    elif ch == "б":
        out.append("а")
    elif ch == "А":
        out.append("Б")
    elif ch == "Б":
        out.append("А")
    else:
        out.append(ch)
print("".join(out))
