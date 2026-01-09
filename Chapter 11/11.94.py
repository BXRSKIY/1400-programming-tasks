def main():
    # 11.94. В массиве хранятся сведения о количестве осадков за каждый день января.
    # Определить количество бездождевых дней (осадки = 0) и
    # среднее количество осадков за дни, когда дождь был.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    days = arr[:31]
    if len(days) < 31:
        days += [0.0] * (31 - len(days))
    no_rain = sum(1 for x in days if x == 0)
    rains = [x for x in days if x > 0]
    avg_rain = sum(rains) / len(rains) if rains else 0.0
    print(no_rain, avg_rain)


if __name__ == "__main__":
    main()
