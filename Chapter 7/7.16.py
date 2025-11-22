def main():
    import sys
    # Дано n, числа b1..b10 и число p. Проверить, что сумма bi < p.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 12:
        raise ValueError("Ожидается n, 10 чисел bi и p")
    n = int(data[0])
    b = data[1:11]
    p = data[11]
    s = sum(b)
    print("YES" if s < p else "NO")


if __name__ == "__main__":
    main()
