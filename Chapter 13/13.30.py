# 13.30. 30 предметов: масса, объем, материал. Определить материал с минимальной плотностью.
# Для материала считаем плотность как (суммарная масса)/(суммарный объем) по всем предметам данного материала.
from collections import defaultdict
mass = defaultdict(float)
vol = defaultdict(float)
for _ in range(30):
    line = input().rstrip("\n")
    parts = line.split()
    m = float(parts[0]); v = float(parts[1]); material = " ".join(parts[2:])
    mass[material] += m
    vol[material] += v
best_mat = None
best_d = None
for mat in mass:
    d = mass[mat] / vol[mat]
    if best_d is None or d < best_d:
        best_d = d
        best_mat = mat
print(best_mat)
