def main():
    # 11.88. Количество осадков, выпавших за каждый день августа, хранится в массиве.
    # Определить среднее количество осадков, выпавших в дни, когда шел дождь (не ноль).
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    rains = [x for x in arr if x > 0]
    if rains:
        avg = sum(rains) / len(rains)
    else:
        avg = 0.0
    print(avg)


if __name__ == "__main__":
    main()
