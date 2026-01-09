# 13.1. Фамилии и имена 25 учеников записаны в двух таблицах. Вывести "Фамилия Имя" по строкам.
# Ввод: 25 фамилий (по одной в строке), затем 25 имен.
surnames = [input().rstrip("\n") for _ in range(25)]
names = [input().rstrip("\n") for _ in range(25)]
for f, n in zip(surnames, names):
    print(f"{f} {n}")
