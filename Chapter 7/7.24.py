def main():
    import sys
    # Даны n, s и числа d1..dn. Проверить, что произведение d_i > s.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 3:
        raise ValueError("Ожидается n, s и хотя бы одно число d")
    n = int(data[0])
    s = data[1]
    if len(data) < 2 + n:
        raise ValueError(f"Ожидается n={n} вещественных чисел d1..dn")
    ds = data[2:2+n]
    prod = 1.0
    for x in ds:
        prod *= x
    print("YES" if prod > s else "NO")


if __name__ == "__main__":
    main()
