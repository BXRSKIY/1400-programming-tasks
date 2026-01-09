def main():
    # 11.99. Количество осадков (в мм), выпавших за каждый день января, хранится в массиве.
    # Определить количество дней, в которые выпало осадков больше, чем в среднем за один день месяца,
    # и напечатать их даты (числа месяца).
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    days = arr[:31]
    if len(days) < 31:
        days += [0.0] * (31 - len(days))
    avg = sum(days) / len(days)
    dates = [i+1 for i, x in enumerate(days) if x > avg]
    print(len(dates))
    print(*dates)


if __name__ == "__main__":
    main()
