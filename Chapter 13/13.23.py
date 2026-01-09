# 13.23. 15 журналов: цена и тираж. Найти среднюю стоимость журналов, тираж которых < 10000.
sum_price = 0.0
cnt = 0
for _ in range(15):
    price, tir = map(float, input().split())
    if tir < 10000:
        sum_price += price
        cnt += 1
print(0 if cnt == 0 else sum_price / cnt)
