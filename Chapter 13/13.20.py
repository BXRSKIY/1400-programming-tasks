# 13.20. 30 автомобилей: мощность (л.с.) и стоимость. Найти общую стоимость авто, у которых мощность > 100.
total = 0.0
for _ in range(30):
    power, cost = map(float, input().split())
    if power > 100:
        total += cost
print(total)
