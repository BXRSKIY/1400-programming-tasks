# 12.52. Дано предложение. Вывести все буквы 'м' и 'н' в нем.
s = input().rstrip("\n")
print("".join(ch for ch in s if ch in ("м", "н")))
