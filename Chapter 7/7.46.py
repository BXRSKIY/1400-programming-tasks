def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if n <= 1:
        raise ValueError("n должно быть больше 1")
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} целых чисел a1..an")
    a = data[1:1+n]
    a1_plus_an = a[0] + a[-1]
    a2_minus_an1 = a[1] - a[-2]
    print(a1_plus_an)
    print(a2_minus_an1)


if __name__ == "__main__":
    main()
