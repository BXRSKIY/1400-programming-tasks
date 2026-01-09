# 13.2. Названия 20 футбольных клубов и городов (в двух таблицах). Напечатать "Клуб Город" по строкам.
clubs = [input().rstrip("\n") for _ in range(20)]
cities = [input().rstrip("\n") for _ in range(20)]
for c, t in zip(clubs, cities):
    print(f"{c} {t}")
