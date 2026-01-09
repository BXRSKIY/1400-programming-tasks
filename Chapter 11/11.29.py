def main():
    # 11.29. В массиве хранится количество осадков,
    # выпавших за каждый день января.
    # Определить, в какие числа месяца осадков не было.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    # январь — 31 день, используем первые 31 значения
    days = arr[:31]
    # дополним нулями при необходимости
    if len(days) < 31:
        days += [0.0] * (31 - len(days))
    no_rain_days = [i + 1 for i, x in enumerate(days) if x == 0]
    print(*no_rain_days)


if __name__ == "__main__":
    main()
