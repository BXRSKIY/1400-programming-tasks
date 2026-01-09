# 13.15. 30 сотрудников: фамилия и адрес. Проверить, есть ли в фирме люди с фамилиями:
# Кузин, Куравлев, Кудин, Кульков, Кубиков. Если есть — напечатать их адреса.
targets = {"кузин","куравлев","кудин","кульков","кубиков"}
for _ in range(30):
    line = input().rstrip("\n")
    parts = line.split()
    surname = parts[0]
    address = " ".join(parts[1:])
    if surname.lower() in targets:
        print(address)
