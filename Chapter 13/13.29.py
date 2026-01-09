# 13.29. 28 государств: численность населения (млн) и площадь (тыс. км^2). Определить максимальную плотность населения.
# Плотность (чел/км^2) пропорциональна pop/area с одинаковым коэффициентом, поэтому достаточно max(pop/area).
max_ratio = None
for _ in range(28):
    pop, area = map(float, input().split())
    ratio = pop / area
    if max_ratio is None or ratio > max_ratio:
        max_ratio = ratio
print(max_ratio)
