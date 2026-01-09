def main():
    # 11.116. Результаты 25 спортсменов в лыжной гонке.
    # Найти результат победителя (максимальный).
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    res = arr[:25]
    if not res:
        print(0.0)
    else:
        print(max(res))


if __name__ == "__main__":
    main()
