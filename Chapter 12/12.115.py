# 12.115. Дано слово. Поменять местами первую из букв 'а' и последнюю из букв 'о'.
# Учесть, что таких букв может не быть.
s = input().rstrip("\n")
i = s.find("а")
j = s.rfind("о")
if i == -1 or j == -1:
    print(s)
else:
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    print("".join(lst))
