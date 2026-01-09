def main():
    # 11.134. Результаты прыжков в длину 15 спортсменов.
    # Определить:
    # а) результат каждого спортсмена (сумму всех попыток? или лучший результат?),
    #    В книге обычно подразумевается лучший результат.
    # Здесь считаем, что для каждого спортсмена задано по три прыжка:
    # a1, a2, a3, ..., a45 (15*3 значений).
    # Вывести лучший результат каждого спортсмена.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    n = 15
    attempts_per = 3
    res = []
    for i in range(n):
        start = i * attempts_per
        block = arr[start:start+attempts_per]
        if not block:
            res.append(0.0)
        else:
            res.append(max(block))
    print(*res)


if __name__ == "__main__":
    main()
