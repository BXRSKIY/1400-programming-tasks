def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        raise ValueError("Ожидается n и n вещественных чисел")
    n = int(data[0])
    if n <= 0:
        raise ValueError("n должно быть положительным")
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} вещественных чисел")
    a = data[1:1+n]
    print(sum(a) / n)


if __name__ == "__main__":
    main()
