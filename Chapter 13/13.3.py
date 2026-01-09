# 13.3. Даны 26 городов и стран, где они находятся. Напечатать города, находящиеся в Италии.
# Ввод: 26 строк вида: "<город> <страна>" (страна — последнее слово в строке).
cities_in_italy = []
for _ in range(26):
    line = input().rstrip("\n")
    if not line:
        continue
    parts = line.split()
    city = " ".join(parts[:-1]) if len(parts) > 1 else parts[0]
    country = parts[-1]
    if country.lower() in {"италия", "italy"}:
        cities_in_italy.append(city)
for city in cities_in_italy:
    print(city)
