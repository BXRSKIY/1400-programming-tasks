def main():
    # 11.141. Год рождения каждого из 30 человек.
    # Определить годы рождения двух самых старших.
    # Самые старшие — с минимальными годами рождения.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    years = arr[:30]
    if len(years) < 2:
        print(*years)
        return
    oldest1 = min(years)
    tmp = years.copy()
    tmp.remove(oldest1)
    oldest2 = min(tmp)
    print(oldest1, oldest2)


if __name__ == "__main__":
    main()
