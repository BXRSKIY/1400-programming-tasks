def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + n or n < 3:
        raise ValueError(f"Ожидается n={n} (>=3) чисел")
    x = data[1:1+n]
    # два максимальных
    max1 = max2 = None
    min1 = min2 = None
    for v in x:
        if max1 is None or v > max1:
            max2 = max1
            max1 = v
        elif max2 is None or v > max2:
            max2 = v
        if min1 is None or v < min1:
            min2 = min1
            min1 = v
        elif min2 is None or v < min2:
            min2 = v
    print(max1, max2)
    print(min1, min2)


if __name__ == "__main__":
    main()
