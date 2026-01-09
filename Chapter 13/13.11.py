# 13.11. Стоимость 20 товаров: рубли и копейки. Сравнить два товара по номерам (1..20), какой дороже.
# Ввод: 20 строк: "<рубли> <копейки>", затем i j.
prices = []
for _ in range(20):
    r, k = map(int, input().split())
    prices.append(r*100 + k)
i, j = map(int, input().split())
a, b = prices[i-1], prices[j-1]
if a > b:
    print(i)
elif b > a:
    print(j)
else:
    print("равны")
