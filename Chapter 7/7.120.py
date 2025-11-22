def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} чисел")
    c = data[1:1+n]
    last = 0
    for i, v in enumerate(c, start=1):
        if v == 25:
            last = i
    print(last)


if __name__ == "__main__":
    main()
