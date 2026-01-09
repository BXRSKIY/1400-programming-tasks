# 13.22. 15 учебных заведений: количество учащихся и тип (школа/техникум/училище).
# Найти общее число учащихся школ.
total = 0
for _ in range(15):
    line = input().rstrip("\n")
    parts = line.split()
    cnt = int(parts[0])
    typ = " ".join(parts[1:]).lower()
    if "школ" in typ:
        total += cnt
print(total)
