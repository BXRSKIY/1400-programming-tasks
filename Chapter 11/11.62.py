def main():
    # 11.62. Осадки за каждый день февраля.
    # Найти общее число осадков, выпавших по чётным числам месяца.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    # день 2 — индекс 1, день 4 — индекс 3 и т. д.
    s = sum(arr[1::2])
    print(s)


if __name__ == "__main__":
    main()
