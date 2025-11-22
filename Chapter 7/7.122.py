def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    m = data[0]
    if len(data) < 1 + m:
        raise ValueError(f"Ожидается m={m} чисел")
    xs = data[1:1+m]
    last = 0
    for i, v in enumerate(xs, start=1):
        if abs(v) % 100 == 12:
            last = i
    print(last)


if __name__ == "__main__":
    main()
