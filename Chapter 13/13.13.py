# 13.13. 20 событий (год, месяц, день). Сравнить два события по времени: какое позже.
# Ввод:
#   20 строк: "год месяц день"
#   затем режим: 'a' или 'b'
#   если 'a': i j (1..20) — сравнить события по номерам
#   если 'b': y1 m1 d1 y2 m2 d2 — сравнить 2 даты, заданные текстом
dates = []
for _ in range(20):
    y, m, d = map(int, input().split())
    dates.append((y, m, d))
mode = input().strip().lower()
def cmp(d1, d2):
    if d1 > d2: return 1
    if d2 > d1: return -1
    return 0

if mode == "a":
    i, j = map(int, input().split())
    d1, d2 = dates[i-1], dates[j-1]
elif mode == "b":
    y1, m1, d1_, y2, m2, d2_ = map(int, input().split())
    d1, d2 = (y1, m1, d1_), (y2, m2, d2_)
else:
    raise SystemExit("mode must be a or b")

c = cmp(d1, d2)
if c == 1:
    print(1)
elif c == -1:
    print(2)
else:
    print("равны")
