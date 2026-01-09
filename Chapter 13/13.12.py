# 13.12. 25 моментов времени (часы, минуты). Сравнить два момента по номерам (1..25), какой раньше.
# Ввод: 25 строк: "<часы> <минуты>", затем i j.
times = []
for _ in range(25):
    h, m = map(int, input().split())
    times.append(h*60 + m)
i, j = map(int, input().split())
a, b = times[i-1], times[j-1]
if a < b:
    print(i)
elif b < a:
    print(j)
else:
    print("равны")
