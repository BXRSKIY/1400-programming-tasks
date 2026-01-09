# 13.6. 20 моделей автомобилей: название и максимальная скорость (км/ч). Вывести названия моделей со скоростью > 180.
for _ in range(20):
    line = input().rstrip("\n")
    if not line:
        continue
    parts = line.split()
    speed = int(parts[-1])
    model = " ".join(parts[:-1]) if len(parts) > 1 else parts[0]
    if speed > 180:
        print(model)
