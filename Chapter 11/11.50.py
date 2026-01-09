def main():
    # 11.50. В массиве хранятся сведения о количестве осадков,
    # выпавших за каждый день сентября (30 значений).
    # Определить:
    #  - сколько осадков выпало за месяц;
    #  - сколько осадков выпадало в среднем за один день
    #    в первую, вторую и третью декады.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    days = arr[:30]
    if len(days) < 30:
        days += [0.0] * (30 - len(days))
    total = sum(days)
    dec1 = days[0:10]
    dec2 = days[10:20]
    dec3 = days[20:30]
    avg1 = sum(dec1) / 10.0
    avg2 = sum(dec2) / 10.0
    avg3 = sum(dec3) / 10.0
    print(total)
    print(avg1, avg2, avg3)


if __name__ == "__main__":
    main()
