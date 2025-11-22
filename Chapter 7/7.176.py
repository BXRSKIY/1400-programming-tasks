def main():
    import sys
    temps = list(map(float, sys.stdin.read().split()))
    if len(temps) < 31:
        raise ValueError("Ожидается 31 температура")
    temps = temps[:31]
    # найдём два дня с минимальными температурами
    indexed = list(enumerate(temps, start=1))
    indexed.sort(key=lambda t: t[1])
    day1 = indexed[0][0]
    if len(indexed) > 1:
        day2 = indexed[1][0]
    else:
        day2 = day1
    print(day1, day2)


if __name__ == "__main__":
    main()
