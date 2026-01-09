# 13.14. 24 момента времени (часы, минуты, секунды). Сравнить два момента по номерам (1..24), какой раньше.
# Ввод: 24 строки: "<часы> <минуты> <секунды>", затем i j.
times = []
for _ in range(24):
    h, m, s = map(int, input().split())
    times.append(h*3600 + m*60 + s)
i, j = map(int, input().split())
a, b = times[i-1], times[j-1]
if a < b:
    print(i)
elif b < a:
    print(j)
else:
    print("равны")
