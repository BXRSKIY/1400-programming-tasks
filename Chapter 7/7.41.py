def main():
    import sys
    # Даны n, числа b1..bn и число p.
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = int(data[0])
    if n <= 0:
        raise ValueError("n должно быть положительным")
    if len(data) < 1 + n + 1:
        raise ValueError(f"Ожидается n={n} чисел b1..bn и число p")
    b = data[1:1+n]
    p = data[1+n]
    s = 0.0
    for x in b:
        if x > p:
            s += x
    print(s)


if __name__ == "__main__":
    main()
