# 13.26. 15 моделей автомобилей: стоимость и тип (легковой или грузовой). Найти среднюю стоимость легковых.
sum_cost = 0.0
cnt = 0
for _ in range(15):
    line = input().rstrip("\n")
    parts = line.split()
    cost = float(parts[0])
    typ = " ".join(parts[1:]).lower()
    if "легк" in typ:
        sum_cost += cost
        cnt += 1
print(0 if cnt == 0 else sum_cost / cnt)
