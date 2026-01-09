# 13.24. 20 моделей авто: стоимость и "возраст" (лет). Найти среднюю стоимость авто с возрастом > 6.
sum_cost = 0.0
cnt = 0
for _ in range(20):
    cost, age = map(float, input().split())
    if age > 6:
        sum_cost += cost
        cnt += 1
print(0 if cnt == 0 else sum_cost / cnt)
