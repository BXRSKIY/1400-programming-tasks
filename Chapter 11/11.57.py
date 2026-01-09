def main():
    # 11.57. Осадки за каждый день июня (30 значений).
    # а) в какой половине июня выпало больше осадков:
    #    в первой (1–15) или во второй (16–30);
    # б) в какую декаду (1–10, 11–20, 21–30) выпало больше всего осадков.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    days = arr[:30]
    if len(days) < 30:
        days += [0.0] * (30 - len(days))
    first_half = sum(days[0:15])
    second_half = sum(days[15:30])
    # печатаем 1, если первая половина больше, 2 — если вторая, 0 — если одинаково
    if first_half > second_half:
        print(1)
    elif second_half > first_half:
        print(2)
    else:
        print(0)
    # декады
    sums_dec = [
        sum(days[0:10]),
        sum(days[10:20]),
        sum(days[20:30]),
    ]
    # номер декады (1,2,3) с максимальной суммой
    max_dec = 1 + max(range(3), key=lambda i: sums_dec[i])
    print(max_dec)


if __name__ == "__main__":
    main()
