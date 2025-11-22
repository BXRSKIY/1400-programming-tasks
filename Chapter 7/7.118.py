def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} чисел")
    a = data[1:1+n]
    first = last = -1
    for i, v in enumerate(a, start=1):
        if v == 10:
            if first == -1:
                first = i
            last = i
    # По условию есть хотя бы одно число 10
    print(last)
    print(first)


if __name__ == "__main__":
    main()
