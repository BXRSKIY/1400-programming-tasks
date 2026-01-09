def main():
    # 11.123. Год рождения 30 человек.
    # Найти первый и последний по номеру самый старший.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    years = arr[:30]
    if not years:
        print(-1, -1)
        return
    oldest = min(years)
    first = last = None
    for i, y in enumerate(years, start=1):
        if y == oldest:
            if first is None:
                first = i
            last = i
    print(first, last)


if __name__ == "__main__":
    main()
